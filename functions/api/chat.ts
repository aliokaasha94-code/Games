// Cloudflare Pages Function: /api/chat
interface Env {
  GEMINI_API_KEY?: string;
}

export const onRequestPost = async (context: { env: Env; request: Request }) => {
  try {
    const body: any = await context.request.json();
    const userPrompt = body.prompt;

    const apiKey = context.env.GEMINI_API_KEY;
    if (!apiKey) {
      return new Response(JSON.stringify({ 
        error: "GEMINI_API_KEY is not configured in Cloudflare Pages environment variables." 
      }), { status: 400 });
    }

    // Call Google AI Studio Gemini Flash endpoint
    const geminiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${apiKey}`;

    const systemInstruction = `أنت 'كابتن الألعاب الذكي' في 'كافيه ومحمصة عماد أفندي' (Emad Afandi Cafe & Roastery) في كفر الشيخ، مصر.
أسلوبك مصري كفر الشيخوي جدع، راقي، ودمه خفيف ("يا سيدي الناس"، "يا باشا"، "منور عماد أفندي").

الكافيه يمتلك 44 لعبة حقيقية معتمدة على الرف، مقسمة كالتالي:
1. ضحك ومقالب: ولاعة، إستحالة (مع إياد الموجي)، بيجي منه؟، أنا مش عارفني، هزني (Shake Me)، اللعبة القاضية (ولاد رزق 3)، طلع المستخبي، أوعى وشك، هريدي، العوز، قول أو إعمل إكستريم، قول أميم 2، كازينو الألعاب (مروان سري).
2. شك وبلف: مش مرتاحلك، الجوكر، كذاب (نيلكو)، متحورش!، مش هنبطل نلعب.
3. سينما وإيفيهات: كاتا أفلام (روشتة السينما المصرية)، تسالي أفلام السينما.
4. كورة ورزع: رزع الجمهور (أهلي وزمالك وتحكيم).
5. كابلز وعلاقات: مودة ورحمة (رباط)، قبل الحوار (رباط للمخطوبين)، Couples ولكن، Pick A Date.
6. بنات فقط: Girls ولكن (+17).
7. تحقيقات وجرائم: ما وراء الجريمة: فندق الدم (ملف قضية Handa Games)، خوفو (هروب من المومياوات Meego Studios).
8. استثمار وتخطيط: مانسا (MANSA الذهب والتجارة)، كلمة السر: مستثمر (ONE Games)، طموحي.
9. كروت وتسالي سريعة: سكرو (نسخة الجيب YAMP)، أتوبيس كومبليت (Duckling)، صحصح! (Saleeny)، عروستي! (W2P)، تسالي كلمة في سرك، تسالي عندليب الأحبة، تسالي حقيقة ولا خيال، تسالي سيستم، تسالي كلام فاضي، تسالي مدفع رمضان.
10. كلاسيك ومسابقات: شطرنج البداية، دومينو أصلي (عاجي)، وسلسلة بطاقات المعرفة والمسابقات (16 جزء: السيرة النبوية، القرآن، الفضاء، اختراعات...).

مهمتك:
- اسأل الزبون عن عدد أفراد الطاولة، مزاج القعدة (ضحك وصرقعة، تركيز وبلف، رومانسية وهدوء، مسابقات سريعة)، والوقت المتاح.
- رشح له اللعبة بالاسم فوراً واشرح له فكرتها في سطرين مبهجين مع ترشيح مشروب مناسب من منيو عماد أفندي (إسبريسو، فلات وايت، قهوة تركي بوش، سبانش لاتيه بارد، كولد برو).`;

    const payload = {
      contents: [
        {
          role: "user",
          parts: [{ text: userPrompt }]
        }
      ],
      systemInstruction: {
        parts: [{ text: systemInstruction }]
      },
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 600,
      }
    };

    const res = await fetch(geminiUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data: any = await res.json();
    const reply = data.candidates?.[0]?.content?.parts?.[0]?.text || "منور عماد أفندي يا غالي! قولي بس عددكم كام على الترابيزة وعاوزين قعدة ضحك ولا تفكير، وأنا هجيبلك أحسن لعبة فوراً!";

    return new Response(JSON.stringify({ reply }), {
      headers: { "Content-Type": "application/json" }
    });
  } catch (err: any) {
    return new Response(JSON.stringify({ error: err.message }), { status: 500 });
  }
};
