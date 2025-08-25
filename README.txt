
# Trading Bot Pocket Pro

Уникален интерфейс (български, стил криптоборса) със:
- Панел със сигнал, увереност %, статистики.
- Таймер за обновяване (60 секунди).
- Интерактивна графика със свещи и стрелки BUY/SELL (Plotly.js).
- Вграден Pocket Option под графиката.
- Готов за Render.

## Как да пуснеш:
1. Качи файловете в GitHub.
2. Render → New Web Service → избери repo.
3. Build: `pip install -r requirements.txt`
4. Start: `python app.py`

Смени логиката в `strategy.py` със собствените си индикатори (EMA, RSI и т.н.) – запази същия интерфейс.
