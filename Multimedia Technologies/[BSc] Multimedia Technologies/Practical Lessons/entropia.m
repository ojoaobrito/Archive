v=(0.0001:0.1:1);

function[h]=entropia(p)
h=((-p).*(log2(p)))-((1-p).*(log2(1-p)));
end
