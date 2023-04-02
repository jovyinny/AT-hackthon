# SMS GPT

SMS GPT ni jukwaa la SMS linalotumia teknolojia ya ChatGPT kutoka OpenAI kujibu maswali na kuwapa watumiaji majibu yanayohusiana na maswali yao. Watumiaji wanaweza kutuma SMS kwa lugha ya Kiswahili na kupata majibu yanayofaa kutoka kwa mfumo wa ChatGPT.

## Mahitaji

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- [OpenAI API key](https://beta.openai.com/signup/)
- [Africa's Talking API key](https://account.africastalking.com/auth/register)

## Jinsi ya Kuanzisha

1. Clone repo hii kwenye kompyuta yako:


2. Nenda kwenye folda ya mradi:
   `cd swahili-sauti`

3. Weka mazingira virtual na usakinishe mahitaji:
```python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
4. Unda faili `.env` kwenye folda ya mradi na uongeze ufunguo wako wa OpenAI API na Africa's Talking API:
```
OPENAI_API_KEY=your_openai_api_key
AFRICAS_TALKING_USERNAME=your_africas_talking_username
AFRICAS_TALKING_API_KEY=your_africas_talking_api_key
```
5.Anzisha programu:
```
python main.py
or python main.py
```

## Matumizi

Baada ya kuanzisha programu, unaweza kutuma SMS kwa namba ya simu iliyo kwenye `main.py` na kupokea majibu kutoka kwa mfumo wa ChatGPT. Programu itapokea SMS, kuchakata ujumbe, na kutuma kwa ChatGPT ili kupata jibu. Kisha, jibu litatumwa kwa mtumiaji kama SMS.

## Leseni

SMS GPT inatolewa chini ya [MIT License](LICENSE).

