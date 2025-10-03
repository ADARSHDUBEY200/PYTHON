#  Tuples are also the collection of heterogenous data types and also immutable in nature;

a = () # empty tuple
b = (1 , ) # single element tuple
c = (1,2,3,4,4,4,5);

print(c[0]);
c[0] = 2;
print(c);
print(c.count(4));
print(c.index(2));
print(c.index(4));
print(type(c));