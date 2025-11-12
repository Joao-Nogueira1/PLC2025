Parser para expressões aritméticas

João Nogueira, pg60227

Resposta: https://github.com/Joao-Nogueira1/PLC2025/blob/main/TPC5/parser.py

<img src="https://github.com/user-attachments/assets/5c42cc7b-5ab5-4207-beb8-429d7c46cac1" width="180">

Explicação: Foi contruído um parser utilizando a seguinte gramática
p1: Exp → T ExpL
p2: ExpL → Op T
p3: | eps
p4: T → F ExpL
p5: F → num
p6: | '(' Exp ')'