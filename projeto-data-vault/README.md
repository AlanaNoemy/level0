# Operação Data Vault — Level 0

## Objetivo
Observar os problemas de acoplamento, validação e reutilização do código monolítico antes de refatorá-lo em MVC, MVP e MVVM.

## Executar
```bash
python vault_caos.py
```
O programa cria `vault_original.db` na pasta de execução.

## Experimentos
1. Cadastre um registro válido com periculosidade entre 1 e 10.
2. Liste os registros cadastrados.
3. Execute novamente e observe a persistência dos dados.
4. Experimente um nível fora de 1 a 10 e observe que é aceito.
5. Em uma execução separada, informe texto no nível e observe o `ValueError`.

## Problemas encontrados
- Interface, acesso ao banco e fluxo do programa na mesma função.
- `int(nivel)` sem tratamento de exceções.
- Ausência de restrição `CHECK` para periculosidade.
- Exibição dependente de índices posicionais.
- Baixa reutilização em outras interfaces.
- Ausência de atualização, remoção e filtro.

## Git
```bash
git init
git add .
git commit -m "chore: adiciona codigo legado do level 0"
```
