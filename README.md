# MVL (many valued logic)

MVL («many valued logic») is a python package which implements different types
of logic systems which use more than 2 values.

## What logic systems are implemented?
The following 3 valued logic systems are supported by MVL:
  - Kleene
  - Priest

The following systems are planned for future support:
  - Łukasiewicz MVL
  - Goedel MVL
  - Bochvar 3VL

## Usage

Using MVL is designed to integrate with existing python infrastructure as much
as possible.

```
  > import mvl.kleene as mvl
  
  > if (mvl.T) print('I'm true!')
  "I'm true!"
  
  > if (mvl.U) print('I'm true!')
  
  > if (mvl.F) print('I'm true!')
  
  > print(mvl.or_(mvl.F, mvl.U))
  Unknown

  > e = mvl.str_parse('? and +')
  Expression('? and +')

  > e.eval()
  Unknown
```
