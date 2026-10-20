# Daruma Jeans — brand feed image prompts

Style: Momotaro-style heritage. Warm, crafted, consistent indigo tones.
Size: **3:4 portrait, 1080 × 1440 px** (Instagram's current grid shape).
Save each result as `my-posts/01.jpg` … `my-posts/12.jpg` (or `.png` / `.webp`). The top row can instead be one panorama, `my-posts/panorama.jpg` (see 01–03). The mockup picks them up automatically on refresh. Any number you haven't made yet shows a white placeholder with the post's name. Post 04 is Tammy's photo and post 05 is Daruma's own "Made in Japan. Crafted by You." photo.

### Brand kit (from `_Branding/Daruma Jeans`)

| | |
|---|---|
| **Logo files for photos** | `brand/` in this folder. White versions for dark photos, navy versions for light backgrounds: `daruma-logo-…`, `daruma-logo-name-tagline-…`, `daruma-name-tagline-…` |
| **Font** | Avenir Next Bold (`Font/avenir-next-bold.ttf` in the brand folder) |
| **Tagline** | Made in Japan. Crafted by You. |
| **Colours** | Navy **#32446D** (main) · Red **#BE0C13** · Pink **#D599A0** |

---

## How to keep the feed looking like one brand

1. **Paste the style block at the end of every prompt.** It's already included in each prompt below. Don't change it between posts.
2. **Lock the look after the first good image.** In Midjourney, use that image as a style reference (`--sref <image URL>`). In ChatGPT or Gemini, keep generating in the same chat and say "same lighting, colour grade and film look as before".
3. **Make 4, keep 1.** Reject anything with plastic skin, extra fingers, warped stitching or garbled text.
4. **Don't let AI draw the logo or any text.** It will get the Daruma logo wrong. Every prompt says "no text, no logos". Add the real logo or any words in Canva/Photoshop afterwards.
5. **Mix the shot types.** The order below alternates close-ups, people and wide workshop shots, so no two neighbouring tiles feel the same in either the 4-column (computer) or 3-column (phone) grid.

### Style block (already in every prompt)

> Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, 3:4 vertical

### Tool add-ons

- **Higgsfield (Nano Banana):** attach your reference images and refer to them as `@Image 1`, `@Image 2`… in the prompt, giving each image one job. Put the jeans first as "MOST IMPORTANT" and place embroidery by landmarks (pocket, side seam, waistband), not "same as the reference". Pick **3:4** in the ratio menu.
- **Midjourney:** add `--ar 3:4 --style raw --v 7` to the end.
- **ChatGPT / DALL·E, Gemini, Firefly:** start with "Create a 3:4 portrait photo:" and paste the prompt.
- **Negative prompt** (Stable Diffusion, Leonardo and similar): `text, letters, logo, watermark, extra fingers, deformed hands, plastic skin, oversaturated, neon, cartoon, CGI, blurry`

---

## The 12 posts

Posts 01–03 are pinned, so they always stay in the top row. That makes them the right place for the **seamless 3-tile panorama** below: new posts never push it out of line.

### 01–03 — Pinned · Campaign panorama: MAKE YOUR OWN JEANS (Higgsfield · Nano Banana)

A clean studio campaign that copies the layout of Momotaro's "WASHI PAPER" post, with Alec in the Wide Fit Selvedge jeans. One image, generated in one go, made of two photos side by side:

- **Tiles 1–2:** one huge close-up of Alec wearing the jeans, from chest to mid-thigh, hands in his pockets, face out of frame. The black t-shirt and dark denim fill the frame, and the red dragon is the hero.
- **Tile 3:** a portrait of Alec from head to knee, looking at the camera.
- **Both:** a plain light-grey studio, soft flat light, no props. All the calm space is for the text.

The **customizing message is carried by the text**: MAKE YOUR OWN JEANS, plus "Designed by you, stitched in Harajuku." The embroidery on the jeans is the proof.

**Final size: 9:4 landscape, 3240 × 1440 px.** Save it as `my-posts/panorama.jpg` and the mockup splits it across the pinned row. Double-click `split-panorama.command` to cut the 3 real posts.

```
┌──────────────┬──────────────┬──────────────┐
│ C            │  MAKE YOUR   │            H │
│ H   black    │  OWN JEANS   │   Alec     A │
│ O  t-shirt   │  designed by │  head to   R │
│ O   ═══ jeans · hands ════  │   knee     A │
│ S     in pockets   [dragon] │            … │
└──────────────┴──────────────┴──────────────┘
  ↑ "CHOOSE · STITCH · WEAR"      "HARAJUKU · TOKYO" ↑
   tile 1          tile 2         tile 3
◄──── left photo · 2160 px ──►◄ right · 1080 ►
```

**Captions** (already in the mockup): left = "Pick your designs…", middle = "Make them with your own hands… book via link in bio", right = "Walk out wearing jeans nobody else has…".

#### Attach these in Higgsfield (Nano Banana), in this order

Both are in the `reference/` folder.

| Tag | File | Its one job |
|---|---|---|
| **@Image 1** | `reference/daruma-DeLWMrRCGW3-1.jpg` (Alec, front, full body) | Alec **and** the jeans from the front: fit, colour, stitching, dragon position |
| **@Image 2** | `reference/daruma-DeLWMrRCGW3-4.jpg` (side view) | The side details: dragon, small gold characters and white flower, and where they sit |

The back view (`-2.jpg`) isn't needed: the torii gate on the back pocket can't be seen in either photo.

#### The prompt · Nano Banana 2.1 · ratio 21:9 · 4K · one image

```
Create one photorealistic wide fashion campaign image made of two photographs side by side, separated by a thin vertical white line at exactly two thirds of the image width. Both photographs are of the same man from @Image 1, shot in the same plain studio with the same light. Minimalist Japanese fashion lookbook style.

LEFT PHOTO, filling the left two thirds: an extreme close up crop of the man from @Image 1, framed from mid chest down to mid thigh. His face is out of frame. He faces the camera straight on, standing still, with both hands relaxed in the front pockets of the jeans. His body is centred horizontally in this photo, and the black t shirt and dark denim fill most of the frame, with only a little plain background at the left and right edges. The waistband sits a little below the middle of the photo. The red dragon on his left thigh is fully visible, sharp, and in focus, and his hands do not cover it.

RIGHT PHOTO, filling the right third: a portrait of the same man from @Image 1, framed from the top of his head down to just below the knees. Keep his face, facial features, hair, skin tone, and body proportions exactly the same as in @Image 1. He stands slightly turned toward the camera, one hand in a front pocket, calm and confident, looking at the camera. He is placed slightly left of centre in this photo, with plain background on the right side. The red dragon and the small gold characters are visible on his left leg.

He wears the same plain black heavyweight t shirt as in @Image 1, untucked, ending at the hip.

MOST IMPORTANT: the jeans from @Image 1 and @Image 2 are a real clothing brand product and must be reproduced exactly as they are, identical in both photographs. Do not redesign, restyle, or reinterpret them. Keep the same very wide, straight leg fit. Keep the same dark indigo raw denim color and texture with no fading or distressing, the same light tan contrast stitching on the pockets, seams, and fly, and the same metal button and rivets as in @Image 1.

EMBROIDERY ON THE JEANS, copy exactly from @Image 1 and @Image 2:
1. DRAGON: one red dragon, standing upright and vertical along the leg, head at the top, on the front of the wearer's left thigh, close to the outer side seam, just below the front pocket and roughly one quarter of the way down from the waistband to the hem. Same shape, red thread color, and size as in @Image 1. There is only one dragon. The wearer's right leg has no embroidery at all.
2. SMALL CHARACTERS: two tiny gold embroidered characters stacked vertically on the outer side of the same leg, below the dragon at about mid thigh, as in @Image 2. Copy them exactly from @Image 2; do not invent other characters or make them bigger.
3. FLOWER: one small white flower with a thin light blue stem on the outer side of the same leg, above the hem, as in @Image 2. It is below the frame of both photographs, so it does not need to be visible.
Do not move any of these to the other leg, the center of the leg, or the knee. Do not turn the dragon sideways. Add no other logos, text, rips, patches, or embroidery on the jeans.

Background: a seamless plain light warm grey studio backdrop in both photographs, with nothing else in it. Soft, even, diffused studio light, subtle natural shadows, muted colors: black, deep indigo, and one red accent. High end campaign photography, sharp focus, realistic fabric texture. No props, no furniture. No text, no logos, no watermark.

Use @Image 1 and @Image 2 only for the man and the jeans. Use a lighter, plainer grey background than the dark grey green one in @Image 1.
```

#### Cropping it to the panorama

Nano Banana's 21:9 is slightly wider than the 9:4 the grid needs. Crop it to **3240 × 1440** so the white line lands exactly at **x = 2160**:

- If the result is 3360 × 1440: crop **80 px off the left** and **40 px off the right**.
- If it's another size, first resize it to 1440 px tall, then crop the left and right edges until the line sits at 2160 and the total width is 3240.

The line has to sit exactly at 2160. If it's off, the portrait gets cut across two tiles when the image is split.

#### If something drifts

- **The dragon turns sideways or moves to the middle of the leg:** add "the dragon is upright, vertical, near the outer side seam just below the pocket, exactly as in @Image 1".
- **Two dragons appear, or the dragon is on the wrong leg:** add a separate line: "only the wearer's left leg has embroidery; the wearer's right leg is plain denim". Remember the wearer's left is on the right side of the picture when he faces the camera.
- **The gold characters come out wrong or too big:** add "the gold characters are tiny accents, smaller than the dragon's head, copied exactly from @Image 2". If they're still wrong, delete item 2. A missing tiny detail looks better than a wrong one.
- **Props or a room appear:** repeat at the end: "plain studio backdrop only, no props, no furniture, no shelves".
- **The background comes out dark like @Image 1:** add "very light warm grey background, almost off-white".
- **The close-up shows his face:** add "the top of the left photo cuts across his chest, below the collarbone".
- **The line is missing or in the wrong place:** add "a clean, straight, thin white vertical line divides the image at exactly two thirds of the width". Or leave it out and draw the line yourself when cropping.
- **One detail is off in a good result:** don't regenerate. Attach the result as a new @Image 1, start the prompt with "Edit @Image 1. Keep everything exactly the same… Change only …", and describe just that one fix.

#### Adding the text (Canva or Photoshop, on the 3240 × 1440 canvas)

Same arrangement as Momotaro: headline and tagline centred on tile 2, logo below them, thin vertical text on the outer tiles.

| Element | Content | Position | Style |
|---|---|---|---|
| Side text, tile 1 | **CHOOSE · STITCH · WEAR** | x ≈ 160, y 300–1150, rotated 90° to run vertically | Avenir Next Bold, ~44 px, letter spacing +20%, white |
| Headline, tile 2 | **MAKE YOUR OWN JEANS** (or two lines: MAKE YOUR / OWN JEANS) | Centred at x = 1620, y ≈ 330, over the black t-shirt | Avenir Next Bold, ~80 px on one line or ~96 px on two, white |
| Tagline, tile 2 | **DESIGNED BY YOU, / STITCHED IN HARAJUKU.** | Centred at x = 1620, just under the headline (y ≈ 440–520) | Avenir Next Bold, ~34 px, letter spacing +8%, white |
| Logo, tile 2 | `brand/daruma-logo-name-tagline-white.png` | Centred at x = 1620, about 300 px wide, y ≈ 580–760 | White version |
| Side text, tile 3 | **HARAJUKU · TOKYO** | x ≈ 3100, y 300–1150, rotated 90°, over the plain background | Same style as the tile 1 side text. Use navy #32446D if the background is very light |

All on-image text is in English because the audience is mostly visitors from abroad.

**Checks before exporting**
- No text or logo crosses the cut lines at x = **1080** and x = **2160**. The photo itself runs across them; the headline, tagline and logo must sit entirely inside tile 2 (x 1080–2160).
- The white text sits over the black t-shirt or dark jeans, not the light background, and it covers neither his hands nor the dragon. Regenerate or edit if it does.
- Each tile still makes sense alone: tile 1 = the jeans up close, tile 2 = the message, tile 3 = the person.
- At phone size each tile is only about 125 px wide, so check the headline is still readable when the canvas is zoomed out.

### Alternative panorama · Workshop room (one continuous scene)

A single wide shot of the whole workshop instead of two photos. Keep the cut-line rules above and tell the story left to right: choose → make → finished.

> Wide panoramic interior of a small Japanese denim workshop in Harajuku Tokyo, one continuous scene arranged as three clear zones from left to right: on the left, a wall of hanging raw indigo denim fabric swatches in many shades with red-line selvedge edges and a customer's hand touching one; in the centre, a Japanese craftsman in an indigo work apron and a smiling customer side by side at a long walnut workbench, pressing a silver laurel wreath button onto raw jeans with a vintage hand press; on the right, a finished pair of raw indigo jeans displayed on a wooden stand with a red and white daruma embroidered on the back pocket, a shelf of small red daruma dolls above, consistent floor and wall running through the whole image, people and key objects placed clearly inside each zone and away from the one-third and two-thirds lines, Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, ultra-wide 9:4 panorama

**Getting 9:4 from other tools:** Midjourney: add `--ar 9:4 --style raw --v 7`. Gemini / Firefly: generate at 16:9, then widen it with *Generative Expand*. ChatGPT: generate at 3:2, then ask it to extend the left and right sides to 9:4.

**Alternative:** if neither panorama works out, use the three single images below instead. Save them as `01`, `02` and `03` and remove `panorama.jpg`.

### 01 — Pinned (alternative) · Choose your denim
**Caption:** Step one: choose your denim. Raw selvedge from Okayama, from 12oz to 21oz. Every roll has its own character.

> A customer's hand running across a row of hanging raw denim fabric swatches in different indigo shades, from deep near-black indigo to lighter blue, each swatch showing its selvedge edge with a thin red line, close-up from the side with the swatches receding into soft focus, Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, 3:4 vertical

### 02 — Pinned (alternative) · The experience
**Caption:** Your jeans, made with your hands. Pick the fabric, the fit, the details — we guide every step in our Harajuku workshop. Booking link in bio.

> A smiling young customer and a Japanese denim craftsman in an indigo work apron standing side by side at a wooden workbench, the craftsman guiding the customer's hands as they press a copper button onto raw selvedge jeans with a vintage hand press, small workshop in Harajuku Tokyo, shelves of folded indigo denim behind them, a small red and white daruma doll on the shelf, candid moment of laughter, Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, 3:4 vertical

### 03 — Pinned (alternative) · The finished pair
**Caption:** Finished. One pair, one owner, one story — embroidered with the Daruma that wishes you luck.

> The back of a new pair of raw indigo selvedge jeans laid flat on a weathered walnut table, the back pocket embroidered with a small red and white daruma doll motif in cotton thread, a blank brown leather waist patch, copper rivets catching the light, a small real daruma doll and a folded unbleached cotton cloth beside the jeans, overhead three-quarter angle, Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, 3:4 vertical

### 04 — Selvedge detail
**Caption:** The red line. Selvedge is woven slowly on vintage shuttle looms, so the edge never frays.

> Extreme macro close-up of a rolled cuff on raw indigo selvedge jeans, showing the clean white selvedge edge with a single red stripe, slubby uneven cotton texture visible in detail, chain-stitch hem threads in mustard yellow, the jeans resting on a dark wooden floor, Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, 3:4 vertical

### 05 — Chain-stitch hemming
**Caption:** Chain-stitch hemming on our Union Special. The rope-like fade it leaves is worth the wait.

> Close-up of a craftsman's weathered hands feeding the hem of raw indigo jeans into a vintage black industrial chain-stitch sewing machine with worn metal parts, mustard yellow thread running through the needle, motion of fabric slightly blurred, workshop bench in the background, Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, 3:4 vertical

### 06 — Shades of indigo
**Caption:** Shades of indigo. Which one is yours?

> A neat stack of eight folded raw denim jeans on an old wooden shelf, arranged from darkest indigo at the bottom to lightest faded blue at the top, each fold showing a selvedge edge and copper rivet, side lighting raking across the fabric texture, Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, 3:4 vertical

### 07 — Customer on the street
**Caption:** Made in the morning, worn in Harajuku by the afternoon. Thank you for making with us.

> A stylish young traveller walking down a quiet Harajuku backstreet in Tokyo wearing new dark raw indigo selvedge jeans with a cuffed hem, plain white t-shirt and canvas tote bag, full body shot from slightly low angle, small shops and green plants softly blurred behind, late afternoon golden light, relaxed natural expression, Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, 3:4 vertical

### 08 — Copper rivets
**Caption:** Copper rivets, set by hand. Small details that hold everything together.

> Macro close-up of a small brass hammer about to strike a copper rivet on the front pocket corner of raw indigo jeans, a few loose copper rivets and burrs scattered on a dark walnut workbench, sharp focus on the rivet, Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, 3:4 vertical

### 09 — Embroidery thread
**Caption:** Choose your thread. Every embroidery is stitched to order — initials, a date, a Daruma.

> Rows of cotton embroidery thread spools on a wooden wall rack in warm colours, red, mustard, cream, rust and indigo, a hand reaching to pick a red spool, an indigo denim pocket with half-finished red embroidery resting on the bench below, Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, 3:4 vertical

### 10 — Flat lay
**Caption:** Everything that goes into one pair.

> Overhead flat lay on a weathered walnut table: a folded pair of raw indigo selvedge jeans, a blank brown leather patch, a handful of copper buttons and rivets, a spool of mustard yellow thread, vintage tailor's scissors, a cloth measuring tape, a blank kraft paper tag on twine, and a small red daruma doll, carefully arranged with generous space between items, Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, 3:4 vertical

### 11 — The workshop
**Caption:** Morning light in the workshop, before the first guests arrive. Open daily, Harajuku, Tokyo.

> Wide interior shot of a small, cosy Japanese denim workshop in the early morning, sunlight streaming through a large window onto wooden workbenches, vintage sewing machines, shelves of folded indigo jeans, hanging fabric swatches and a row of red daruma dolls on a high shelf, empty and quiet, dust in the light beams, Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, 3:4 vertical

### 12 — Fades over time
**Caption:** Two years of wear. Raw denim remembers how you live — that's the point.

> Close-up of well-worn indigo selvedge jeans showing high-contrast honeycomb fades behind the knee and whiskers at the hip, faded light blue creases against deep indigo, the person standing against a plain warm plaster wall, Japanese heritage denim brand photography, warm natural window light, deep indigo and raw selvedge denim tones, warm walnut wood and aged brass accents, muted earthy palette of indigo, unbleached cotton, walnut brown and copper, soft 35mm film grain, shallow depth of field, shot on a 50mm lens, calm premium editorial mood, realistic textures, no text, no logos, no watermark, 3:4 vertical

---

## Using your own photos instead

Any of the 12 can be a real photo from the shop instead. Shoot it portrait (3:4), near a window, and match the shot description above. Then save it with the same number. To make real photos sit with the AI ones, give them the same edit: slightly warm white balance, lowered blue saturation, lifted shadows and a little grain.
