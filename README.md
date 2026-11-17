# Celestial Letter

*A little letter from the stars, written for you each day.*

Celestial Letter is a daily astrology project built for Hack Club's TRMNL. It uses your birth information to calculate your natal planetary positions, compares them with the current sky, and turns the most significant planetary aspects into a short daily reading.

Instead of giving you a generic horoscope based only on your Sun sign, I wanted to explore something more personal: how the planets in your birth chart interact with the planets moving through the sky today.

## What does it do?

- **Natal Chart:** Calculates planetary positions using your birth date, time, and location.
- **Daily Transits:** Compares your natal chart with current planetary positions.
- **Aspect Detection:** Finds major aspects, including conjunctions, sextiles, squares, trines, and oppositions.
- **Daily Interpretations:** Matches planetary aspects with written interpretations.
- **A Personal Letter:** Selects up to two of the closest aspects and turns them into a short letter for the day.

When there aren't any significant aspects with available interpretations, the letter gives you a quieter message instead.

## How it works

1. Your birth information is used to calculate your natal planetary positions.
2. The program retrieves the current planetary positions.
3. It compares both charts and calculates the angular distance between planets.
4. Major aspects are identified based on their angular deviation.
5. The closest aspects are ranked and matched with interpretations.
6. Everything is assembled into a daily letter.

## Run it yourself

Clone the repository:

```bash
git clone https://github.com/winnyT/celestial-letter.git
cd celestial-letter
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Set an API key for the protected API endpoint:

```bash
export CELESTIAL_API_KEY="your-secret-key"
```

Start the application:

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

### API

The daily letter can also be requested through:

`POST /api/daily-letter`

Example request:

```bash
curl -X POST http://127.0.0.1:5000/api/daily-letter \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $CELESTIAL_API_KEY" \
  -d '{
    "name": "Alex",
    "birth_date": "2000-09-22",
    "birth_time": "14:30",
    "birth_place": "Hanoi",
    "timezone": "Asia/Ho_Chi_Minh"
  }'
```

## Things I want to add

- [ ] Finish the TRMNL polling integration.
- [ ] Let users save their own birth information.
- [ ] Improve the daily interpretation library.
- [ ] Add more detailed readings for Moon, rising sign, and other natal chart placements.
- [ ] Refine the letter layout for the e-ink screen.

## Why I made this

I've always liked the idea of receiving a little letter every day (fyi: it's my love languages xD). Something that feels personal, rather than another notification telling me what to do.

I also wanted to learn more about astrology beyond the usual Sun sign horoscopes. There are so many relationships between planets in a birth chart, and I thought it would be interesting to turn those relationships into something readable.

This project became a way for me to explore astronomy-related calculations, Python, APIs, and designing for an e-ink display all at once.

It's still a work in progress, but I like where it's going.

---

Made with 🖤 for Hack Club's TRMNL project.
