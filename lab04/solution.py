der winner(names, scores):
  top = 0
  for i in range(1, len(scores)):
    if scores[i] > scores[top]:
      top = i
  return names[top]
