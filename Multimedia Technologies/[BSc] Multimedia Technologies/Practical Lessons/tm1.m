A = [1, 2, 3, 4; 5, 6, 7, 8; 9, 10, 11, 12];
B = A(2,2);
A(3,2)=10;
C = A(2,:); %linha n da matriz A
D = A (:,2); %coluna n da matriz A
