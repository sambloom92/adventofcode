from day_8.utils import BootCode, get_boot_code


class CodeFixFailed(Exception):
    pass


def fix_code(code_original):
    """
    fix the code by swapping a single nop and jmp command at different lines of the code
    :param code_original: the original broken code
    :return: the value of the accumulator for the fixed code when run
    """
    for index in range(len(code_original)):
        code_modified = code_original.copy()
        if "acc" in code_modified[index]:
            pass
        else:
            code_modified[index] = (
                code_modified[index]
                .replace("nop", "placeholder")
                .replace("jmp", "nop")
                .replace("placeholder", "jmp")
            )
            boot_code = BootCode(code_modified)
            boot_code.run()
            terminated = boot_code.terminated
            if terminated:
                return boot_code.accumulator
    raise CodeFixFailed


if __name__ == "__main__":
    code = get_boot_code()
    print(fix_code(code))
