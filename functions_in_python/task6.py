larger = lambda a, b: a if a > b else b

print(f"larger(10, 20) = {larger(10, 20)}")   # Should output 20
print(f"larger(-5, -10) = {larger(-5, -10)}")  # Should output -5
print(f"larger(8, 8) = {larger(8, 8)}")     # Should output 8
