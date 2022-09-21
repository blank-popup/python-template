SOUNDS_FIRST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
SOUNDS_MIDDLE = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
SOUNDS_LAST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def split_korean_consonant_vowel(phrase):
    period_first = len(SOUNDS_MIDDLE) * len(SOUNDS_LAST)
    period_middle = len(SOUNDS_LAST)
    rv = []
    for letter in phrase:
        if '가' <= letter <= '힣':
            print(letter)
            index_letter = ord(letter) - ord('가')
            index_first = index_letter // period_first
            index_middle = (index_letter - period_first * index_first) // period_middle
            index_last = index_letter - period_first * index_first - period_middle * index_middle
            print(index_letter, index_first, index_middle, index_last)
            rv.append([SOUNDS_FIRST[index_first], SOUNDS_MIDDLE[index_middle], SOUNDS_LAST[index_last]])
        else:
            rv.append([letter])
    return rv

def print_korean_unicode_value():
    def print_letter_unicode_hex(letter):
        value = ord(letter)
        print(f'[{letter}]: [{value}] [{hex(value)}]')
    print(f'===== 처음과 끝 =====')
    print_letter_unicode_hex('가')
    print_letter_unicode_hex('힣')
    print(f'===== 초성 =====')
    for l in SOUNDS_FIRST:
        print_letter_unicode_hex(l)
    print(f'===== 중성 =====')
    for l in SOUNDS_MIDDLE:
        print_letter_unicode_hex(l)
    print(f'===== 종성 =====')
    for l in SOUNDS_LAST:
        print_letter_unicode_hex(l)
