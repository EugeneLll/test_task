import sys


def check_jumps(nums: list[int]) -> bool:
    curr_jump = nums[0]
    for num in nums[1:]:
        if curr_jump == 0:
            return False
        curr_jump = max(curr_jump - 1, num)
    return True


if __name__ == "__main__":
    nums = [int(num) for num in sys.argv[1].strip("[]").replace(" ", "").split(",")]
    print(check_jumps(nums))
