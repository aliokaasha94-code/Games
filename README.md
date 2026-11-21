# ☕ ألعاب كافيه عماد أفندي (Emad Afandi Games Hub) 👑

المنصة الرقمية التفاعلية لعرض وشرح واختيار ألعاب الطاولة والكروت في **كافيه عماد أفندي** بكفر الشيخ.

---

## 🌟 ميزات المنصة (Key Features)

- 📱 **Mobile-First PWA:** تجربة تصفح سريعة وخفيفة جداً مصممة خصيصاً لهواتف الزبائن على الطاولات.
- 🎨 **هوية بصرية ملكية (Notion Brand System):** مستوحاة من أرشيف هوية عماد أفندي (الذهبي الملكي `#D4AF37`، وخلفيات الإسبريسو الفاخرة `#0B0B0C`، وحدود الـ 1px الذهبية المضيئة).
- 🔍 **بحث وفلترة فورية:** تصفية الألعاب حسب عدد أفراد القعدة (2 لعيبة، 3-4، 5-6، شلة 8+)، أو حسب الفئة (ضحك، كابلز، شك، كورة، سينما).
- 📜 **دليل القوانين وطريقة اللعب:** نافذة سفلية (Bottom-Sheet) لكل لعبة تشرح القواعد خطوة بخطوة بالعامية المصرية الودودة وقوانين الفوز والعقوبات.
- 🤖 **كابتن الألعاب الذكي (AI Concierge):** شات بوت مدعوم بنماذج Gemini من Google AI Studio؛ يفهم طبيعة القعدة وبميزة **Function Calling** يقوم تلقائياً بفتح وترشيح كارت اللعبة على شاشة الزبون فوراً!
- ☁️ **معمارية سحابية نقية على Cloudflare ($0 Overhead):**
  - استضافة الواجهة: **Cloudflare Pages**.
  - قاعدة البيانات: **Cloudflare D1** (Serverless SQLite على أسرع شبكة Edge في مصر).
  - الأصول والصور: **Cloudflare R2** بصيغة `WebP` فائقة الضغط والخفة (أقل من 30KB).

---

## 🛠️ التشغيل والتطوير المحلي (Local Development)

```bash
# 1. تثبيت الحزم
npm install

# 2. تشغيل سيرفر التطوير المحلي
npm run dev

# 3. بناء النسخة الإنتاجية السحابية لـ Cloudflare Pages
npm run build

# 4. معاينة البناء الإنتاجي
npm run preview
```

---

## ☁️ النشر على Cloudflare Pages وقاعدة بيانات D1

### 1. إنشاء وتهيئة قاعدة بيانات D1:
```bash
# إنشاء قاعدة البيانات في حساب Cloudflare
npx wrangler d1 create emad-afandi-games-db

# تطبيق السكيما والفهارس
npx wrangler d1 execute emad-afandi-games-db --file=schema.sql

# إدخال بيانات الألعاب الأولية (26+ لعبة)
npx wrangler d1 execute emad-afandi-games-db --file=seed.sql
```

### 2. النشر السريع على Cloudflare Pages:
```bash
npx wrangler pages deploy dist --project-name=emad-afandi-games
```

---

## 🖼️ مسار توليد الصور في Google Flow عبر المتصفح الداخلي

1. الدخول إلى `flow.google.com` عبر **متصفح Antigravity المدمج**.
2. اختيار نموذج **Nano Banana 2.1** (0 رصيد) أو **Omni Flash** برصيد الـ PRO المتاح.
3. استخدام البرومبت المعتمد:
   ```text
   A cinematic, ultra-photorealistic product shot of the board game box "[GAME_NAME]" placed gracefully on a rich dark rustic oak cafe table inside an upscale Egyptian cafe. In the background, warm moody amber ambient lighting, soft golden bokeh lights, an authentic Emad Afandi ceramic espresso cup with rising steam, and a subtle golden royal emblem. Hyper-detailed textures, realistic cardboard print reflections, tactile card components fanned out neatly, luxury boutique atmosphere, 8k resolution, shot on 85mm lens f/1.8.
   ```
4. تحويل الصورة الناتجة إلى `.webp` ونقلها إلى مجلد `public/games/`.

---

## 👑 حقوق الملكية والهوية
- **المالك:** كافيه عماد أفندي.
- **الرئيس التنفيذي:** إبراهيم عماد العطيان.
- **التطوير والحلول التقنية:** علي عكاشة (Ali Okasha).
- **الموقع الرسمي:** [emadafandi.com](https://emadafandi.com)
- **خدمة العملاء والواتساب:** [+20 10 3403 1919](tel:+201034031919)
