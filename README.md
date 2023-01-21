# unrpa - Extract files from the RPA archive format.

[![GitHub](https://img.shields.io/github/license/varieget/unrpa)](https://github.com/varieget/unrpa/blob/master/COPYING)
[![MyPy Check](https://github.com/varieget/unrpa/actions/workflows/typecheck.yml/badge.svg)](https://github.com/varieget/unrpa/actions/workflows/typecheck.yml)

## 关于

unrpa 用于解压由 [Ren'Py Visual Novel Engine](https://www.renpy.org/) 打包的 RPA 文件。

此 repo 是 `Lattyware/unrpa` 的一个 fork，主要面向 furry 类型的 Ren'Py 游戏。

## 使用

请 [下载最新的源码](https://api.github.com/repos/varieget/unrpa/zipball/master) 并解压出来。

需要 Python 3.7 或更高版本。

If you are trying to extract more exotic RPA archives, there may be additional dependencies. unrpa should instruct you how to install them if required.

### 示例

- 在 macOS 或 Linux，打开终端，确保当前工作目录在 unrpa 然后：

```bash
python3 -m unrpa -mp "path/to/output/dir" "path/to/archive.rpa"
```

- 在 Windows，打开 cmd，确保当前工作目录在 unrpa 然后：

```bash
py -3 -m unrpa -mp "path\to\output\dir" "path\to\archive.rpa"
```

### 适配情况

#### 默认支持

RPA-1.0, RPA-2.0, RPA-3.0, ALT-1.0, ZiX-12A, ZiX-12B, RPA-3.2, RPA-4.0

#### 额外支持

| 游戏名         |                          | RPA Header                          |
| -------------- | ------------------------ | ----------------------------------- |
| 厷雏           | GrandNesting-demo-1.0-pc | `ENC-1.0 cccccccccc81e99egdededede` |
| 罗曼圣诞探案集 | Romans Christmas         | `PLZ-3.0 0000000000db034b 42424242` |

## Command line usage

```
usage: unrpa [-h] [-v] [-s] [-l | -t] [-p PATH] [-m] [--version]
             [--continue-on-error] [-f VERSION] [-o OFFSET] [-k KEY]
             FILENAME [FILENAME ...]
```

### Options

| Positional Argument | Description                |
| ------------------- | -------------------------- |
| FILENAME            | the archive(s) to extract. |

| Optional Argument    | Description                                                               |
| -------------------- | ------------------------------------------------------------------------- |
| -h, --help           | show this help message and exit                                           |
| -v, --verbose        | explain what is being done, duplicate for more verbosity (default: 1).    |
| -s, --silent         | no non-essential output.                                                  |
| -l, --list           | list the contents of the archive(s) in a flat list.                       |
| -t, --tree           | list the contents of the archive(s) in a tree view                        |
| -p PATH, --path PATH | extract files to the given path (default: the current working directory). |
| -m, --mkdir          | will make any missing directories in the given extraction path.           |
| --version            | show program's version number and exit                                    |

| Advanced Argument           | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| --continue-on-error         | try to continue extraction when something goes wrong.    |
| -f VERSION, --force VERSION | ignore the archive header and assume this exact version. |
| -o OFFSET, --offset OFFSET  | ignore the archive header and use this exact offset.     |
| -k KEY, --key KEY           | ignore the archive header and use this exact key.        |

## Errors

### Common errors

- Check you are using the latest version of Python 3.
- Check you are using quotes around file paths.
- Video guides may be out of date, please check this file for up-to-date advice on using the tool.

### New errors

需要支持新的游戏，或者解压时出现错误，请 [提出 issue](https://github.com/varieget/unrpa/issues)。

New variants of the RPA format get created regularly, so new games might not work - generally support can be added quickly though.
