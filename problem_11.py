function get(arr, y, x) {

  if (0 <= y && y < arr.length && 0 <= x && x < arr[y].length) {
    return arr[y][x];
  }
  return 0;
}

function solution(arr, k) {

  var max = 0;

  for (var y = 0; y < arr.length; y++) {
    for (var x = 0; x < arr.length; x++) {

      var p1 = 1, p2 = 1, p3 = 1, p4 = 1;

      for (var i = 0; i < k; i++) {
        p1*= get(arr, y, x + i);
        p2*= get(arr, y + i, x);
        p3*= get(arr, y + i, x + i);
        p4*= get(arr, y + i, x - i);
      }
      max = Math.max(p1, p2, p3, p4, max);
    }
  }
  return max;
}
solution(arr, 4);
