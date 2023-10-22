package main

import (
	"crypto/sha256"
	"encoding/hex"
	"flag"
	"fmt"
	"io"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
)

func getFlags() (bool, bool, bool) {
	compilerOnly := flag.Bool("c", false, "Only compile the script without running it")
	forceCompilation := flag.Bool("fc", false, "Forces the file to be compiled, useful for version mismatches")
	interpreterOnly := flag.Bool("i", false, "Only interpreter the script without compiling it")

	flag.Parse()
	if *interpreterOnly && *compilerOnly {
		*interpreterOnly = false
		*compilerOnly = false
	}

	return *compilerOnly, *forceCompilation, *interpreterOnly
}

func getFile() string {
	args := os.Args[1:]
	if !(len(args) >= 1) {
		fmt.Println("Please supply a NoBash script to run")
		os.Exit(1)
	}
	return args[len(args)-1]
}

func checkFileName(file string) {
	if !strings.HasSuffix(file, ".nb") {
		fmt.Println("Specified file '" + file + "' is not a NoBash (.nb) file")
		os.Exit(2)
	}
}

func checkFileExistence(file string) {
	_, err := os.ReadFile(file)
	if err != nil {
		fmt.Println("Could not read file '" + file + "'")
		os.Exit(3)
	}
}

func getFileHash(fileName string) string {
	file, err := os.Open(fileName)
	if err != nil {
		fmt.Printf("Could not read file '%s'\n", fileName)
		os.Exit(7)
	}
	defer file.Close()
	hash := sha256.New()
	_, err = io.Copy(hash, file)
	if err != nil {
		fmt.Printf("Can't copy data from file '%s'", fileName)
		os.Exit(8)
	}
	return hex.EncodeToString(hash.Sum(nil))
}

func getCompiledPath() string {
	homePath, err := os.UserHomeDir()
	if err != nil {
		fmt.Println("Can't get home directory of current user!")
	}
	return homePath + "/.nobash/compiledScripts/"
}

func checkFileCompiled(file string) bool {
	path := getCompiledPath()
	files, err := os.ReadDir(path)
	if err != nil {
		fmt.Println("No directory '~/.nobash/compiledScripts/'")
		os.Exit(4)
	}
	for _, compiledScript := range files {
		if compiledScript.Name() != file+"c" {
			continue
		}
		lines, err := os.ReadFile(path + compiledScript.Name())
		if err != nil {
			fmt.Println("Failed to open file at '" + path + compiledScript.Name() + "'")
			os.Exit(6)
		}
		linesList := strings.Split(string(lines), "\n")
		for _, line := range linesList {
			if strings.HasPrefix(line, "filehash, ") {
				compiledHash := line[len("filehash, "):]
				fileHash := getFileHash(file)
				if compiledHash == fileHash {
					return true
				}
			}
		}
	}
	return false
}

func checkFile(file string) bool {
	checkFileName(file)
	checkFileExistence(file)
	return checkFileCompiled(file)
}

func compile(file string, executablePath string, forceCompilation bool) {
	alreadyCompiled := checkFile(file)
	if !alreadyCompiled || forceCompilation {
		cmd := exec.Command("python3", executablePath+"/compiler.py", file)
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		err := cmd.Run()
		if err != nil {
			if exiterr, ok := err.(*exec.ExitError); ok {
				os.Exit(exiterr.ExitCode())
			} else {
				fmt.Println("[NoBash ]Something went wrong while compiling: ", err.Error())
				os.Exit(15)
			}
		}
	}
}

func reverseString(str string) string {
	result := ""
	for _, char := range str {
		result = string(char) + result
	}
	return result
}

func getExecutablePath() string {
	executablePath, _ := os.Executable()
	lastSlash := len(executablePath) - 1 - strings.Index(reverseString(executablePath), "/")
	return executablePath[:lastSlash]
}

func getBaseFile(file string) string {
	return filepath.Base(file)
}

func interpret(file string) {
	executablePath := getExecutablePath()
	compiledPath := getCompiledPath()
	file = getBaseFile(file)
	cmd := exec.Command("python3", executablePath+"/interpreter.py", compiledPath+file+"c")
	cmd.Stdout = os.Stdout
	cmd.Stdin = os.Stdin
	cmd.Stderr = os.Stderr
	cmd.Run()
}

func main() {
	executablePath := getExecutablePath()
	compilerOnly, forceCompilation, interpreterOnly := getFlags()
	file := getFile()
	if !interpreterOnly {
		compile(file, executablePath, forceCompilation)
	}
	if !compilerOnly {
		interpret(file)
	}
}
