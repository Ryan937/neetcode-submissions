class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        Stack<Character> stack = new Stack<>();
        helper(result, stack, 0, 0, n);

        return result;
    }

    public void helper(List<String> result, Stack<Character> stack, int open, int close, int n) {
        if (open == close && open == n) {
            StringBuilder builder = new StringBuilder();

            for (char c : stack)
                builder.append(c);

            result.add(builder.toString());
            return ;
        }

        if (open < n) {
            stack.push('(');
            helper(result, stack, open + 1, close, n);
            stack.pop();
        }

        if (close < open) {
            stack.push(')');
            helper(result, stack, open, close + 1, n);
            stack.pop();
        }
    }
}
