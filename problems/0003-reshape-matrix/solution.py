import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	total_element = sum(len(row) for row in a )
	target_elements = new_shape[0] *new_shape[1]
	if total_element != target_elements:
		return []
	return np.array(a).reshape(new_shape).tolist()