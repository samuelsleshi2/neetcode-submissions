class Solution {
    public boolean isValid(String s) {
        //initializes stack
        Stack<Character> stack = new Stack<>();
        if (s.charAt(0) == ')' || s.charAt(0) == '}' || s.charAt(0) == ']' ) {
                return false;
            }
        // Iterates through string
        for (int i = 0; i < s.length(); i++) {
            
            // Stacks the open brackets
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[' ) {
                stack.push(s.charAt(i));
            }
            else {
                if (stack.isEmpty()){
                    return false;
                }
                char d = stack.pop();
                if (s.charAt(i) == ')') {
                    if (d != '(') {
                        return false;
                    }
                }
                else if (s.charAt(i) == ']') {
                    if (d != '[') {
                        return false;
                    }
                }
                else if (s.charAt(i) == '}') {
                    if (d != '{') {
                        return false;
                    }
                }
            }

        }
        return stack.isEmpty();
    }
}
