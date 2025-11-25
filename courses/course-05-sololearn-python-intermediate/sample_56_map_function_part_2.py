'''
The map function requires the first argument to be a function and the second argument to be an iterable.
'''


exam_scores = [85, 62, 95, 40, 78]


def is_passing(score):
  return score >= 70


status = list(map(is_passing, exam_scores))

print(status)