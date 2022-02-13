audioinfo('C:\Users\a37880\Desktop\bass.wav'); audioinfo('C:\Users\a37880\Desktop\drums.wav'); audioinfo('C:\Users\a37880\Desktop\guitar.wav');
[bass,Fbass]=audioread('C:\Users\a37880\Desktop\bass.wav');
d=length(bass)/Fbass; %duração do som
bass1=bass(1:Fbass); %1 segundo 
bass2=(Fbass+1:Fbass*2); %2 segundo
bass12=((Fbass*11)+1:Fbass*12); %12 segundo
bass12Vezes4=[bass12;bass12;bass12;bass12];
bass_seg=bass(44100*10 + 1:44100*20);
[drums,Fdrums]=audioread('C:\Users\a37880\Desktop\drums.wav');
[guitar,Fguitar]=audioread('C:\Users\a37880\Desktop\guitar.wav');
sound(bass,Fbass);
clear sound; %parar o áudio que está a ser reproduzido
