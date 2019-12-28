# 3VL

3VL («3 valued logic») is a python package which implements different types of 3
valued logic systems.

## What types of 3 valued logic are implemented?
The following 3 valued logic systems are supported by 3VL:
[None yet]

The following systems are planned for future support:
  - Kleene
  - Priest
  - Łukasiewicz

## Usage

Using 3VL is designed to integrate with existing python infrastructure as much
as possible.

```
  > import tvl.kleene as tvl
  
  > if (tvl.T) print('I'm true!')
  "I'm true!"
  
  > if (tvl.U) print('I'm true!')
  
  > if (tvl.F) print('I'm true!')
  
  > print(tvl.or_(tvl.F, tvl.U))
  Unknown

  > e = tvl.str_parse('? and +')
  Expression('? and +')

  > e.eval()
  Unknown
```
