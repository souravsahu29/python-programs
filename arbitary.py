def function(num1, num2, *args, **kwargs):
    print(f"num1: {num1} & num2: {num2}\n args: {args}\n kwargs: {kwargs}")


function(1,2,23, 73, 12, name='Sourav', day=2)
