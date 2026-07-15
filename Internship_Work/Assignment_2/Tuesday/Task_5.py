def count_digits_in_number(s: str) -> int:
	"""Count digit characters in the input string representing a number."""
	return sum(1 for ch in s if ch.isdigit())


def main():
	s = input().strip()
	# If input is empty, consider 0 digits
	if not s:
		print(0)
		return
	print(count_digits_in_number(s))


if __name__ == "__main__":
	main()

