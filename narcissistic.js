//checking if a given number is narcissistic
//problem info: https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/javascript
function narcissistic(value) {
  valueStr = value.toString(10);
  n = valueStr.length;
  narNum = 0;
  for (i = 0; i < n; i++)
      narNum += Math.pow(parseInt(valueStr[i]),n);
  if (value==narNum)
    return true;
  else
    return false;
}
