# Project Documentation: WC Tool Coding Challenge

This documentation outlines the development process of the WC Tool project, designed to mimic the functionality of the Unix `wc` command. Each section below details specific commits that collectively map the evolution and implementation of the project according to the requirements of the [coding challenge](https://codingchallenges.fyi/challenges/challenge-wc).


# How to Run the Project

## Requirements
- Ensure Python 3.x is installed on your machine.

## Running the Tool
To run the tool, navigate to the root directory of the project and use the following syntax:

### From a File
To execute the tool with a file as input:

```python3 -m src test.txt [options]```

Where [options] can be:
- -l: Count lines
- -w: Count words
- -c: Count characters

If no options are specified, the tool will perform all counts (lines, words, and characters) by default.

Example:
```python3 -m src test.txt -w```
This command counts the words in test.txt.

### From Standard Input
To use input from another command:

```cat test.txt | python3 -m src [options]```

This method allows integration with other commands or processing output from other programs.

Example:
```cat test.txt | python3 -m src -l```
This command will count the lines in test.txt using the output piped from the cat command.

## Feature Development

### Initial Project Structure + First Step of the Challenge
- **Commit**: [Step One wc challenge -c](https://github.com/DavidOrtegaFarrerons/wc-tool-cc/commit/68c1f1febe2d81a723409db5af448630c2d361d3)
  - **Description**: Added minimal functions to display the first step working, which shows the total bytes of a file.

### Modular Structure Enhancement
- **Commit**: [Add folders to separate logic](https://github.com/DavidOrtegaFarrerons/wc-tool-cc/commit/d7a6157017ca4b0d2aa8b7b22a7f79c34edd2a96#diff-5745cb7d8ed87db31cdaef7ff6d897c0bcaf2200967146f11d0e1728540ea0b5)
  - **Description**: Reorganized project structure into separate folders to enhance modularity and understandability of the code.

### Line Counting
- **Commit**: [Feature: add -l option to count lines](https://github.com/DavidOrtegaFarrerons/wc-tool-cc/commit/3115112d291ccdf2de908c6ed57283707cb3bf23)
  - **Description**: Added the line count feature, along with some small naming refactors to improve code readability.

### Small Refactor
- **Commit**: [Refactor](https://github.com/DavidOrtegaFarrerons/wc-tool-cc/commit/578b2a4d5cb9dbaa392a11528273dce53a10558e)
  - **Description**: Enhanced documentation on tool functionality and usage.

### Word Counting
- **Commit**: [Feature: Add argument -w to count words of a file](https://github.com/DavidOrtegaFarrerons/wc-tool-cc/commit/2fc08486345466b5023f05debc763c9bcee8000e)
  - **Description**: Created a separate service responsible for counting the words in a given file.

### Character Counting
- **Commit**: [Feature: Add argument -m to count characters of a file](https://github.com/DavidOrtegaFarrerons/wc-tool-cc/commit/ad85f7546d5267edf0ab52d3dd266703e2f5f459)
  - **Description**: Created a service responsible for counting the characters in a file.

### Default Option Handling
- **Commit**: [Feature: Implement default option](https://github.com/DavidOrtegaFarrerons/wc-tool-cc/commit/ecb819903eac2c0f65f5e37fcfc00d0fef146be7)
  - **Description**: Implemented a default option to execute line, word, and character counts if no specific argument is provided.

## Refinements and Optimizations

### Argument Dispatch Optimization
- **Commit**: [Refactor: Optimize argument_dispatch](https://github.com/DavidOrtegaFarrerons/wc-tool-cc/commit/fa1239f235a3a1b02ec7db247acafd63bd721506)
  - **Description**: Optimized the argument dispatch mechanism using a key-value map, reducing unnecessary conditionals.

### Argument Dispatch Optimization 2
- **Commit**: [Refactor: Optimize argument_dispatch with constants](https://github.com/DavidOrtegaFarrerons/wc-tool-cc/commit/3e53507344900ec2fa6efdaa6ced1277f44bc86f)
  - **Description**: Further optimized the argument dispatch mechanism by adding constants to enhance code readability.

### Final Touches and Completion
- **Commit**: [Finish last step from CodingChallenge](https://github.com/DavidOrtegaFarrerons/wc-tool-cc/commit/bc355e4f6652e8bc352e910977e93d4382157907)
  - **Description**: Completed the final step of the coding challenge, refined the code for better performance, and integrated handling of stdin with a TemporaryFile.

## Conclusion
This project has significantly enhanced my understanding of Python, marking my first substantial engagement with the language.
