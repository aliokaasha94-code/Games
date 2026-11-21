// Cloudflare Pages Function: /api/chat (Hardened, Secure & Fast)
interface Env {
  GEMINI_API_KEY?: string;
}

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

export const onRequestOptions = async () => {
  return new Response(null, { headers: CORS_HEADERS });
};

export const onRequestPost = async (context: { env: Env; request: Request }) => {
  try {
    const apiKey = context.env.GEMINI_API_KEY;
    if (!apiKey) {
      return new Response(
        JSON.stringify({ error: "خدمة كابتن الألعاب الذكي قيد التهيئة." }),
        { status: 503, headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' } }
      );
    }

    // Input Validation & Size Guard
    let body: any;
    try {
      body = await context.request.json();
    } catch {
      return new Response(
        JSON.stringify({ error: "صيغة الطلب غير صالحة." }),
        { status: 400, headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' } }
      );
    }

    const userPrompt = typeof body?.prompt === 'string' ? body.prompt.trim() : '';
    if (!userPrompt || userPrompt.length > 500) {
      return new Response(
        JSON.stringify({ error: "يرجى كتابة رسالة واضحة لا تتجاوز 500 حرف." }),
        { status: 400, headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' } }
      );
    }

    // Call Google Gemini API with header-based authorization (No key leaked in URL!)
    const geminiUrl = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent';

    const systemInstruction = `أنت 'كابتن الألعاب الذكي' في 'كافيه عماد أفندي' (Emad Afandi Cafe) في كفر الشيخ، مصر.
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
10. كلاسيك ومسابقات: شطرنج البداية، دومينو أصلي (عاجي)، وسلسلة بطاقات المعرفة والمسابقات (16 جزء).

مهمتك:
- اسأل الزبون عن عدد أفراد الطاولة، مزاج القعدة (ضحك وصرقعة، تركيز وبلف، رومانسية وهدوء، مسابقات سريعة)، والوقت المتاح.
- رشح له اللعبة بالاسم فوراً واشرح له فكرتها في سطرين مبهجين مع ترشيح مشروب مناسب من منيو عماد أفندي (إسبريسو، فلات وايت، قهوة تركي بوش، سبانش لاتيه بارد، كولد برو).`;

    const payload = {
      contents: [{ role: "user", parts: [{ text: userPrompt }] }],
      systemInstruction: { parts: [{ text: systemInstruction }] },
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 400,
      }
    };

    const res = await fetch(geminiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-goog-api-key": apiKey
      },
      body: JSON.stringify(payload)
    });

    if (!res.ok) {
      return new Response(
        JSON.stringify({
          reply: "منور يا غالي في عماد أفندي! قولي بس عددكم كام ومزاجكم ضحك ولا تفكير، وهختارلك أحسن لعبة فوراً!"
        }),
        { headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' } }
      );
    }

    const data: any = await res.json();
    const reply = data.candidates?.[0]?.content?.parts?.[0]?.text || "أهلاً بيك في عماد أفندي! حدد عددكم ونوع القعدة وهساعدك فوراً.";

    return new Response(JSON.stringify({ reply }), {
      headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' }
    });
  } catch {
    return new Response(
      JSON.stringify({ error: "حدث خطأ غير متوقع، يرجى المحاولة لاحقاً." }),
      { status: 500, headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' } }
    );
  }
};
