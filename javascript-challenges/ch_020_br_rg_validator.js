
function descobrirDigito(rg) {
  var digitos = rg.split("");
  var totais = [];
  var total = 0;

  // Multiplicamos os que seriam da primeira linha com os da segunda    
  digitos.forEach(function (digito, index) {
      totais.push(Number(digito) * (2 + index));
  });

  // Multiplicamos as colunas
  totais.forEach(function(numero) { total += numero });

  // Descobrimos o resto da divisão
  var resto = total % 11;

  return 11 - resto;
}

console.log(descobrirDigito("14862954"));