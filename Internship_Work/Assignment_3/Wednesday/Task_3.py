
def main():
	employees = {
		'Ali': 70000,
		'Ahmed': 55000,
		'Saad': 62000,
	}

	# Display each employee and salary using items()
	for name, salary in employees.items():
		print(f"{name}: {salary}")


if __name__ == '__main__':
	main()
