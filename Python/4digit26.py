def is_all_even_digit(n):
   return all (int(digit)%2==0 for digit in str(n))
def generate_even_digit_square(start,end):
  """Generate a list of four_digit numbers that are perfct squares with all even digits"""
  even_digit_squares=[]
  start_sqrt = int(start**0.5)
  end_sqrt = int(end**0.5)+1
  for i in range(start_sqrt,end_sqrt):
    square=i*i
    if square>=start and square<=end and is_all_even_digit(square):
       even_digit_squares.append(square)
  return even_digit_squares
start_range=1000
end_range=9999
result=generate_even_digit_square(start_range,end_range)
print'the four_digit_numbers that are perfect squares with all even digits are:',result

