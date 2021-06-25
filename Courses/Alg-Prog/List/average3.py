N1, N2, N3, N4 = input().split()
N1, N2, N3, N4 = float(N1), float(N2), float(N3), float(N4)

media = ((N1*2) + (N2*3) +   (N3*4) + (N4*1)) / (2+3+4+1)
print(f'Media: {media:.1f}')

if media >= 7.0:
    print('Aluno aprovado.')
if media < 5.0:
    print('Aluno reprovado.')
if 5.0 <= media <= 6.9:
    print('Aluno em exame.')
    notadoexame = float(input())
    print(f'Nota do exame: {notadoexame}')

    mediafinal = (media + notadoexame) / 2

    if mediafinal >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {mediafinal:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {mediafinal:.1f}')