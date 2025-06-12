const fs = require('fs');
const path = require('path');
const vsctm = require('vscode-textmate');
const oniguruma = require('vscode-oniguruma');

const wasmBin = fs.readFileSync(path.join(__dirname, './node_modules/vscode-oniguruma/release/onig.wasm')).buffer;
const vscodeOnigurumaLib = oniguruma.loadWASM(wasmBin).then(() => {
    return {
        createOnigScanner(patterns) { return new oniguruma.OnigScanner(patterns); },
        createOnigString(s) { return new oniguruma.OnigString(s); }
    };
});

const scopeName = "source.sdoc";
const grammarPath = path.join(__dirname, "syntaxes/sdoc.tmLanguage.json");
const filePath = process.argv[2];
if (!fs.existsSync(filePath)) {
  throw('File does NOT exist');
}

// Create a registry that can create a grammar from a scope name.
const registry = new vsctm.Registry({
  onigLib: vscodeOnigurumaLib,
  loadGrammar: (scope) => {
    if (scope === scopeName) {
      const grammarData = fs.readFileSync(grammarPath, 'utf-8');
      return Promise.resolve(vsctm.parseRawGrammar(grammarData, grammarPath));
    }
    return null;
  }
});

registry.loadGrammar(scopeName).then(grammar => {
    const lines = fs.readFileSync(filePath, 'utf-8').split(/\r?\n/);
    let ruleStack = vsctm.INITIAL;

    lines.forEach((line, lineIndex) => {
      const lineTokens = grammar.tokenizeLine(line, ruleStack);
      ruleStack = lineTokens.ruleStack;

      lineTokens.tokens.forEach(token => {
        const tokenText = line.slice(token.startIndex, token.endIndex);
        console.log(`[${lineIndex + 1}:${token.startIndex}-${token.endIndex}] "${tokenText}" → ${token.scopes.join(' ')}`);
      });
    });
  });
