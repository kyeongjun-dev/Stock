import yfinance as yf

# 티커로 현재가격 return
def get_current_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.info
    if 'ask' not in data.keys():
        return "ask not found"
    else:
        return data['ask']

# 내가 보유중인 종목
stock_list = {
    'KBSTAR미국S&P500': '379780.KS',
    'KBSTAR미국S&P500(H)': '453330.KS',
    '맥쿼리인프라': '088980.KS',
    'ACE미국배당다우존스': '402970.KS',
    'SOL미국배당다우존스': '446720.KS',
    'KODEX미국나스닥100(H)': '449190.KS',
    'SOL미국배당다우존스(H)': '452360.KS',
    'ACE미국30년국채액티브(H)': '453850.KS',
    'TIGER미국배당다우존스': '458730.KS',
    'KBSTAR미국30년국채엔화노출(합성H)': '472870.KS',
    'SOL미국나스닥100': '476030.KS',
    '프로텍': '053610.KS',
    '범한퓨얼셀': '382900.KS',
    '삼기이브이': '419050.KS',
    'TIGER일본엔선물': '292560.KS',
    '아이온큐': 'IONQ',
    'TLT': 'TLT',
    '리얼티인컴': 'O',
    '로켓랩': 'RKLB',
    'SPLG': 'SPLG',
    '마이크로소프트': 'MSFT',
    '아마존': 'AMZN',
    '엔비디아': 'NVDA',
    '팔란티어': 'PLTR',
    'QQQM': 'QQQM',
}

# 구글시트 기입순서
arr = [    
    'TIGER일본엔선물',
    'ACE미국배당다우존스',
    'KBSTAR미국30년국채엔화노출(합성H)',
    '아이온큐',
    'TLT',
    '리얼티인컴',
    '로켓랩',
    'SPLG',
    '맥쿼리인프라',
    'TIGER일본엔선물',
    'KBSTAR미국S&P500',
    'ACE미국배당다우존스',
    'SOL미국배당다우존스',
    'KODEX미국나스닥100(H)',
    'SOL미국배당다우존스(H)',
    'KBSTAR미국S&P500(H)',
    'ACE미국30년국채액티브(H)',
    'TIGER미국배당다우존스',
    'KBSTAR미국30년국채엔화노출(합성H)',
    'SOL미국나스닥100',
    'KODEX미국나스닥100(H)',
    'SOL미국배당다우존스(H)',
    'KBSTAR미국S&P500(H)',
    '리얼티인컴',
    '마이크로소프트',
    '아마존',
    '아이온큐',
    '엔비디아',
    '팔란티어',
    'QQQM',
    'SPLG',
    'TLT',
]

for stock_name in arr:
    print(get_current_price(stock_list[stock_name]))