a=imread('C:\Users\a37880\Desktop\Imagens_Alunos\PGM\boats.png'); %"a" é um array
imfinfo('C:\Users\a37880\Desktop\Imagens_Alunos\PGM\boats.png'); %detalhes da imagem
a=imresize(a,0.5); a=a(1:2:end,1:2:end,:); %reduzir a imagem a metade (o ":" significa "manter o que já está", neste caso manter os 3 canais de cor)
a=imresize(a,2); b=b(1:0.5:end,1:0.5:end,:); %ampliar a imagem 2 vezes
a=imcrop(a,[200,200,200,200]); a=a(200:1:400,200:1:400); %recortar uma secção da imagem
b(200:1:400,200:1:400)=a; %colocar um bloco de uma imagem noutra imagem
a=imcomplement(a); %colocar cores negativas na imagem
a=imrotate(a,90); a=a'; %rodar a imagem 90º (para a direita)
b=flip(b,2); c=b(:,end:-1:1); %inversão horizontal
b=flip(b,1); c=b(end:-1:1,:); %inversão vertical
imhist(b); %histograma da imagem (para o intervalo de 0 a 255 níveis de cinza, ver quantos píxeis existem em cada valor deste intervalo)
histeq(b); %histograma equalizado da imagem
im2bw(c) %threshold da imagem (destaca os contrastes da imagem, serve para distinguir o fundo dos objetos da frente)

%para imagens a cor, basta usar os 3 canais de cor (usar ":" para manter os canais)
