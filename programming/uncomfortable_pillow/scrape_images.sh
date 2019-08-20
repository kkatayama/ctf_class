# https://www.dcode.fr/gravity-falls-bill-cipher
# https://gravityfalls.fandom.com/wiki/List_of_cryptograms/Books#Bill.27s_symbol_substitution_cipher

for i in {65..90}; do curl 'https://www.dcode.fr/tools/gravity-falls-bill/images/char('$i').png' -H 'Referer: https://www.dcode.fr/gravity-falls-bill-cipher' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36 OPR/62.0.3331.119' -o $i.png ; done;
