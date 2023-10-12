'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

'''
def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        res  = [""]*numRows
        row, col = 0, 1

        for ch in s:
            res[row] += ch

            if row == 0:
                col = 1
            elif row == numRows - 1:
                col = -1
            
            row += col
        return "".join(res)
