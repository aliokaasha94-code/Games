-- Cloudflare D1 Seed Script for Emad Afandi Games Hub
-- Run with: npx wrangler d1 execute emad-afandi-games-db --file=seed.sql

INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'mesh-mertahlak',
    'مش مرتاحلك',
    'Mesh Mertahlak',
    'قول أميم (2oolameme)',
    'https://2oolameme.com',
    'bluffing',
    'شك وبلف',
    4,
    10,
    '+14',
    '30-45 دقيقة',
    'متوسط',
    'تعرف تاكل بعقلهم حلاوة؟ ولا هتتكشف من أول كارت؟',
    'لعبة الشك الأولى في القعدة! كروت مواقف وبلوفات تخليك تشك في أقرب صاحب ليك. اللعبة بتختبر مين بيعرف يمثل بثقة ومين وشه بيفضحه أول ما يكدب.',
    '1. كل لاعب بياخد كروته في السر.
2. بتنزل كارت وتدعي إنه مطابق لشرط الجولة بدون ما تكشفه.
3. لو حد حس إنك بتكذب هيقولك ''مش مرتاحلك!''.
4. لو طلعت كذاب بتاكل الكروت كلها، لو طلعت صادق هو اللي بيشيل الكروت وينزل مكانه عقاب.',
    'الفايز هو أول واحد يتخلص من كروته كلها بدون ما يتكشف بلفه، والخسران بيلبس كروت الجزاء كلها.',
    '/games/mesh-mertahlak.webp',
    '["صحاب", "بلف", "تمثيل", "شك", "سهرة طويلة", "ضحك"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'el-joker',
    'الجوكر',
    'El Joker',
    'Lucid Dreaming Games',
    'https://luciddreaminggames.com',
    'bluffing',
    'شك وبلف',
    3,
    8,
    '+14',
    '15-20 دقيقة',
    'ذكاء وسرعة',
    'كثير من الأقنعة.. وقليل من الوجود!',
    'لعبة استنتاج وبلوف مصرية ممتعة جداً. أقنعة وشخصيات سرية يتم تبادلها على الطاولة، وكل لاعب بيحاول يحقق هدفه السري ويكشف مين الجوكر الحقيقي قبل ما يقلب الطاولة على الكل.',
    '1. يتم توزيع كروت الأقنعة مقلوبة على كل لاعب.
2. كل لاعب في دوره بيستخدم قدرة القناع اللي معاه (أو يدعي إنه معاه القناع ده!).
3. لو حد شك فيه بيتحداه: لو صادق بيكسب أفضلية ولو كاذب بيخسر قناعه.
4. الجوكر بيفوز لو نجح يخدع القعدة كلها للنهاية.',
    'لعبة سريعة الإيقاع، كل جولة بتاخد 15 دقيقة ومليانة حماس وتخمين.',
    '/games/el-joker.webp',
    '["استنتاج", "أقنعة", "ذكاء", "سريعة", "تحدي"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'kadab',
    'كذاب (KADAB)',
    'Kadab',
    'نيلكو (Nilco)',
    'https://nilco-int.com',
    'bluffing',
    'شك وبلف',
    3,
    6,
    '+8',
    '20 دقيقة',
    'سهل',
    'اكشف الكذاب.. واهرب من ألعاب العذاب!',
    'لعبة ورق كلاسيكية بروح عصرية من نيلكو. بتنزل كروت مقلوبة وتعلن عن قيمتها، بس هل أنت صادق ولا بتلف؟ لو حد قال عليك كذاب وكشفك هتشيل الطاولة كلها!',
    '1. وزع الكروت بالتساوي على اللاعبين.
2. كل لاعب بينزل كارت أو أكتر مقلوبين ويقول رقم.
3. اللاعب اللي بعده يقرر: يصدق وينزل كروت أعلى، أو يقول ''كذاب!'' ويكشف الورق.',
    'أول لاعب يخلص كل ورقه يفوز فوراً.',
    '/games/kadab.webp',
    '["نيلكو", "ورق", "كذاب", "ضحك", "سريعة"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'met7awech',
    'متحورش!',
    'Met-7awech',
    'Eftah Topic',
    'https://eftahtopic.net',
    'bluffing',
    'شك وبلف',
    3,
    8,
    '+14',
    '25 دقيقة',
    'سهل وذكي',
    'متحورش عليا.. كدبتك مكشوفة من قبل ما تنطق!',
    'لعبة صراحة وبلوف مصرية خفيفة الظل من Eftah Topic. كروت مواقف محرجة واختبارات تخليك تكشف مين في الشلة بيحور وبيألف حوارات ومين بيتكلم جد.',
    '1. اسحب كارت السؤال المحرج.
2. احكي موقف حصل معاك حقيقي أو ألف حكاية محبوكة.
3. باقي القعدة تصرخ ''متحورش!'' لو حسوا إنك بتألف، أو يصدقوك وتكسب النقطة.',
    'اللي يتحفش وهو بيحور بيلبس حكم فوري من القعدة.',
    '/games/met7awech.webp',
    '["متحورش", "صراحة", "حكايات", "ضحك", "صحاب"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'msh-hanbatel-nel3ab',
    'مش هنبطل نلعب',
    'Msh Hanbatel Nel3ab',
    'RAW Entertainment',
    'https://2oolameme.com',
    'bluffing',
    'شك وبلف',
    3,
    8,
    '+14',
    '30 دقيقة',
    'سهل وحماسي',
    'النسخة الملحقة باللعبة القاضية.. مكملين لعب وضحك للصبح!',
    'الإصدار المميز المكمل للعبة ولاد رزق ''مش هنبطل نلعب''! كروت حيل وتحديات وعمليات توريط بين الصحاب على طاولات الكافيه.',
    '1. اسحب كارت العملية أو المقلب.
2. طبق التحدي على أقرب لاعب ليك في القعدة.
3. أول واحد ينفذ 3 عمليات ناجحة يكسب الجولة.',
    'لعبة سريعة ومليانة ضحك وروح شبابية.',
    '/games/msh-hanbatel.webp',
    '["ولاد رزق", "تحديات", "ضحك", "صحاب"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'wala3a',
    'ولاعة',
    'Wala3a',
    'قول أميم (2oolameme)',
    'https://2oolameme.com',
    'comedy',
    'ضحك ومقالب',
    3,
    8,
    '+14',
    '20-30 دقيقة',
    'سهل جداً',
    'اختبار حقيقي لغدر الصحاب.. القعدة هتشعلل!',
    'لعبة بتولع القعدة بالمعنى الحرفي! كل كارت بيسأل سؤال محرج أو بيفرض تصويت على أكتر واحد في الشلة فيه صفة معينة، وطبعاً التوريط شغال والضحك ملوش سقف.',
    '1. اسحب كارت من الرزمة في النص واقراه بصوت عالي.
2. الكارت بيطلب تصويت جماعي على 3.. 2.. 1 والكل بيشاور على شخص في القعدة.
3. اللي بياخد أعلى أصوات بياخد كارت الولاعة.
4. اللي بيجمع 5 ولاعات هو اللي بيولع في العقاب النهائي للشلة!',
    'لا يوجد حياد! التصويت إجباري، وسحب الكارت ملزم للجميع بدون زعل.',
    '/games/wala3a.webp',
    '["ضحك", "غدر الصحاب", "توريط", "سريعة", "شلة شباب"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'est7ala',
    'إستحالة (مع إياد الموجي)',
    'Est7ala - Eyad Elmogy',
    'قول أميم (2oolameme) & إياد الموجي',
    'https://2oolameme.com',
    'comedy',
    'ضحك ومقالب',
    3,
    10,
    '+14',
    '25-35 دقيقة',
    'سهل ومضحك جداً',
    'مع صانع المحتوى إياد الموجي.. مواقف وسيناريوهات إستحالة تصدقها!',
    'لعبة الحفلات الكوميدية الأحدث بالتعاون مع صانع المحتوى المصري الشهير إياد الموجي! كروت سيناريوهات جنونية ومواقف مستحيلة، وكل لاعب عليه يقنع القعدة باختياره أو يلبس في عقاب إستحالة ينفذه.',
    '1. اسحب كارت السيناريو المستحيل.
2. اختار بين أمرين أحلاهما مر ومستحيل.
3. الشلة بتصوت وتجادل، واللي اختياره شاذ عن إجماع القعدة بياخد كارت العقاب.',
    'الضحك هو البطل، وممنوع الهروب من الإجابة الصريحة!',
    '/games/est7ala.webp',
    '["إياد الموجي", "إستحالة", "ضحك", "شلة", "تحديات", "يوتيوب"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'byegy-menno',
    'بيجي منه؟',
    'Byegy Menno?',
    'قول أميم (2oolameme)',
    'https://2oolameme.com',
    'comedy',
    'ضحك ومقالب',
    3,
    8,
    '+14',
    '25 دقيقة',
    'سهل جداً',
    'هل صاحبك ده بيجي منه؟ ولا فستكة على الفاضي؟',
    'لعبة التحديات والتقييمات المضحكة من قول أميم! كروت بتختبر مهارات ومواهب غريبة عند أفراد الشلة (تمثيل، غناء، تقليد، مواقف ضغط)، وباقي القعدة تقرر: هل بيجي منه ولا ميجيش منه خالص!',
    '1. اسحب كارت التحدي واقرأ الموقف أو الموهبة المطلوبة.
2. اللاعب ينفذ التحدي قدام الشلة في 30 ثانية.
3. القعدة بتصوت بكروت ''بيجي منه'' أو ''ميجيش منه''.',
    'صاحب أعلى عدد كروت ''بيجي منه'' هو نجم القعدة.',
    '/games/byegy-menno.webp',
    '["بيجي منه", "قول أميم", "ضحك", "مواهب", "تحديات", "صحاب"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'ana-mesh-arafny',
    'أنا مش عارفني',
    'Ana Mesh 3arafny',
    'قول أميم (2oolameme)',
    'https://2oolameme.com',
    'comedy',
    'ضحك ومقالب',
    3,
    8,
    '+12',
    '20-30 دقيقة',
    'سهل وممتع',
    'أنا مين؟ وإيه اللي جابني هنا؟ تخمين هويات وإحراج للصبح!',
    'لعبة تخمين الهويات والشخصيات الشهيرة المستوحاة من أغنية عبد الباسط حمودة الأيقونية! كل لاعب بيتحط على راسه أو قدامه كارت شخصية ميعرفهاش، ولازم يخمن هو مين من أسئلة ذكية للصحاب.',
    '1. كل لاعب بياخد كارت مقلوب على جبهته بدون ما يشوفه.
2. في دورك بتسأل الشلة أسئلة بنعم أو لا (أنا ممثل؟ أنا عايش؟ أنا شرير؟).
3. أول واحد يعرف شخصيته الحقيقية يكسب الكارت.',
    'سرعة الاستنتاج وسؤال الأسئلة الذكية هي اللي هتوصلك للحل.',
    '/games/ana-mesh-arafny.webp',
    '["أنا مش عارفني", "قول أميم", "تخمين", "ضحك", "شخصيات"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'shake-me',
    'Shake Me! (هزني)',
    'Shake Me',
    'JokeyJoy',
    'https://jokeyjoy.com',
    'comedy',
    'ضحك ومقالب',
    3,
    10,
    '+12',
    '25 دقيقة',
    'سهل جداً',
    '6 ألعاب في بوكس واحد.. مش محتاج غير صباع وضحك!',
    'بوكس أسطواني تفاعلي فيه فتحة يد تسحب منها كروت التحديات. اللعبة بتضم 6 ألعاب مصغرة حركية وسرعة رد فعل ومواقف كوميدية غير متوقعة.',
    '1. اهز العلبة واسحب كارت من الفتحة العلوية.
2. شوف نوع اللعبة من الـ 6 ألعاب (سرعة بديهة، تمثيل بصباع، إشارات، أسئلة محرجة).
3. نفذ في التايمر المحدد أو اتعرض للعقاب الجماعي من القعدة.',
    'أكتر لعبة بتعمل جو وحركة وتفاعل على الترابيزة لكسر الملل فوراً.',
    '/games/shake-me.webp',
    '["تفاعلي", "حركة", "ضحك", "شلة كبيرة", "كسر جليد"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'el-le3ba-el-qadya',
    'اللعبة القاضية (ولاد رزق 3)',
    'El Le3ba El Qadya - Welad Rizk 3',
    'RAW Entertainment & 2oolameme',
    'https://2oolameme.com',
    'comedy',
    'ضحك ومقالب',
    3,
    8,
    '+16',
    '35 دقيقة',
    'متوسط وحماسي',
    'القاضية ممكن! لعبة ولاد رزق الرسمية.. غدر وعمليات وسيطرة!',
    'لعبة الأكشن والعمليات المستوحاة من فيلم ولاد رزق 3! خطط لعملية سرقة، وزع الأدوار على الشلة، واستعد للغدر من أقرب صاحب ليك عشان ينفرد بالغنائم.',
    '1. جهز كروت الخطة والأسلحة والهروب.
2. نفذ العملية مع شركائك، بس خلي عينك على كروت الغدر.
3. اللي يضرب القاضية في التوقيت الصح يستحوذ على الغنيمة كلها!',
    'لا تثق بأحد في عالم ولاد رزق!',
    '/games/el-le3ba-el-qadya.webp',
    '["ولاد رزق", "أكشن", "غدر", "القاضية", "ضحك", "صحاب"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'tala3-el-mostakhabby',
    'طلع المستخبي',
    'Tala3 El Mostakhabby',
    'قول أميم (2oolameme)',
    'https://2oolameme.com',
    'comedy',
    'ضحك ومقالب',
    3,
    8,
    '+14',
    '25 دقيقة',
    'سهل',
    'مفيش حاجة هتفضل متدارية.. كل الفضايح على الترابيزة!',
    'لعبة الصراحة والاعترافات المحرجة من قول أميم! أسئلة غير متوقعة وتحديات كشف المستور اللي بتخلي القعدة كلها تضحك على مواقف زمان وحواديت الشلة اللي محدش كان يعرفها.',
    '1. اسحب كارت المستخبي واقرأ السؤال بصوت عالي.
2. جاوب بصراحة أو ادفع كارت غرامة واعمل التحدي المكتوب.
3. أجرأ لاعب في القعدة بيكسب لقب بطل الصراحة.',
    'الصراحة هي العملة الوحيدة المقبولة على الترابيزة!',
    '/games/tala3-el-mostakhabby.webp',
    '["طلع المستخبي", "قول أميم", "صراحة", "فضايح", "ضحك"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'ew3a-weshak',
    'أوعى وشك',
    'Ew3a Weshak',
    'قول أميم (2oolameme)',
    'https://2oolameme.com',
    'comedy',
    'ضحك ومقالب',
    3,
    8,
    '+12',
    '20 دقيقة',
    'سهل وسريع',
    'سرعة بديهة وردود أفعال مباغتة.. أوعى وشك يروح في داهية!',
    'لعبة ردود الأفعال والمقالب الصاروخية! كروت أكشن مفاجئة بتتطلب حركة فورية أو تقليد صوت أو قصف جبهة في جزء من الثانية، واللي يتأخر بيشيل العقاب.',
    '1. ارمي الكروت في النص بسرعة وبشكل متتابع.
2. أول ما يظهر كارت ''أوعى وشك'' نفذ الحركة المطلوبة فوراً.
3. أبطأ رد فعل في الطاولة يلم الكروت كلها.',
    'لعبة بتعمل دوشة وحماس وضحك عالي جداً.',
    '/games/ew3a-weshak.webp',
    '["أوعى وشك", "سرعة", "رد فعل", "ضحك", "حركة"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'hareedy',
    'هريدي (Hareedy)',
    'Hareedy Party',
    'Meego Studios',
    'https://meegostudios.com',
    'comedy',
    'ضحك ومقالب',
    2,
    8,
    '+8',
    '15 دقيقة',
    'سهل ومضحك',
    'هريدي الصعيدي الجدع.. طابق الجلابية والشنب قبل الكل!',
    'لعبة سرعة ملاحظة ومطابقة كوميدية بشخصية هريدي الصعيدي المحبوبة من Meego Studios. كروت ملونة بالجلابيب والعمم والشنبات المختلفة، والمطلوب سرعة صيد الكارت المطابق.',
    '1. كارت هريدي الأساسي في النص.
2. كل لاعب بيحاول يرمي كارت مطابق في لون الجلابية أو شكل الشنب.
3. أول واحد ينزل كروته كلها ويصرخ ''يا هريدي!'' يكسب الجولة.',
    'ممنوع الغلط! الرمية الغلط بتكلفك سحب كارتين جزاء.',
    '/games/hareedy.webp',
    '["هريدي", "ميجو", "ضحك", "سرعة", "شعبي"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'el-3awz',
    'العوز (الكوز)',
    'El 3awz',
    'نيلكو (Nilco)',
    'https://nilco-int.com',
    'comedy',
    'ضحك ومقالب',
    3,
    6,
    '+10',
    '30 دقيقة',
    'متوسط',
    'عربيات فول وتكاتك ومقالب.. مين هيلم الحساب الأول؟',
    'لعبة كروت شعبية بطابع مصري أصيل من نيلكو! مليانة شخصيات من الشارع المصري ومواقف كوميدية، وتجميع طلبات ومقالب تسحب بيها القرشينات من جيوب صحابك.',
    '1. كل لاعب بيحاول يجمع مجموعات كروت متكاملة.
2. استخدم كروت الأكشن والمقالب لتعطيل خصومك وسرقة أكلاتهم ومواردهم.
3. أول واحد يقفل متطلبات اللعبة بدون ما يلبس في العوز يكسب الدور.',
    'لعبة تكتيكية خفيفة ممتعة جداً ومناسبة لكل الأعمار.',
    '/games/el-3awz.webp',
    '["شعبي", "نيلكو", "ضحك", "مقالب", "عائلي"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    '2ool-aw-e3mel',
    'قول أو إعمل إكستريم',
    '2ool Aw E3mel Extreme',
    'قول أميم (2oolameme)',
    'https://2oolameme.com',
    'comedy',
    'ضحك ومقالب',
    3,
    10,
    '+16',
    '35 دقيقة',
    'سهل وتحدي عالي',
    'الحقيقة الصادمة أو التحدي الجريء.. إصدار إكستريم الأقوى!',
    'النسخة الكبيرة والأكثر جرأة من لعبة الصراحة والتحدي الشهيرة! كروت أسئلة محرجة جداً وتحديات تمثيلية وجسدية تخلي القعدة تشتعل حماس وضحك هستيري.',
    '1. اختار: ''قول'' (صراحة) أو ''إعمل'' (تحدي).
2. لو انسحبت من التنفيذ، البس في عقاب إكستريم من اختيار باقي اللاعبين.
3. اللي يجمع 5 كروت تحديات ناجحة يفوز.',
    'ممنوع التراجع بعد الاختيار!',
    '/games/2ool-aw-e3mel.webp',
    '["قول أو إعمل", "إكستريم", "تحدي", "صراحة", "ضحك"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    '2oolameme-2',
    'قول أميم (الجزء التاني)',
    '2oolameme Part 2',
    'قول أميم (2oolameme)',
    'https://2oolameme.com',
    'comedy',
    'ضحك ومقالب',
    3,
    12,
    '+14',
    '30 دقيقة',
    'سهل ومضحك',
    'ملك الميمز المصرية.. اختار أظبط ميم على الموقف!',
    'الجزء الثاني من اللعبة الأسطورية قول أميم! كروت صور ميمز مصرية شهيرة وكروت مواقف حياتية، وكل لاعب بيحاول يطابق أضحك ميم يعبر عن الموقف المكتوب.',
    '1. الحكم يسحب كارت الموقف ويقراه بصوت عالي.
2. كل لاعب يرمي كارت ميم من إيده مقلوب.
3. الحكم يقلب الميمز ويختار أكتر ميم موّت القعدة من الضحك، وصاحبه ياخد النقطة.',
    'أول لاعب يجمع 5 كروت مواقف هو سيد الميمز في عماد أفندي.',
    '/games/2oolameme-2.webp',
    '["قول أميم", "ميمز", "ضحك", "كوميديا", "شلة كبيرة"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'casino-al3ab-marwan-serry',
    'كازينو الألعاب (مروان سري Vol 2)',
    'Casino Al3ab - Marwan Serry',
    'كازينو الألعاب (Casino Al3ab)',
    'https://casinoal3ab.com',
    'comedy',
    'ضحك ومقالب',
    3,
    10,
    '+12',
    '35 دقيقة',
    'متوسط',
    'نسخة مروان سري الرسمية.. 3 ألعاب في لعبة واحدة مش سهلة ومش صعبة!',
    'مستوحاة من برنامج كازينو الألعاب الشهير مع مروان سري وهشام عفيفي! بتجمع بين سرعة البديهة، وتحديات الجرس، وأسئلة كروية وفنية ترفع الأدرينالين.',
    '1. بتنقسم القعدة لفريقين مع حكم أو جرس.
2. سحب كروت التحديات من الفئات التلاتة.
3. أسرع فريق يضغط الجرس أو يجاوب صح بياخد الكارت، واللي يغلط بيلبس كارت أحمر!',
    'الفريق اللي يجمع أكتر نقط قبل نهاية الوقت هو بطل الكازينو.',
    '/games/casino-al3ab.webp',
    '["مروان سري", "كازينو", "كورة", "تحديات", "جرس", "شلة"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'kataflam',
    'كاتا أفلام (Kataflam)',
    'Kataflam',
    'كاتا أفلام الرسمية',
    'https://kataflam.com',
    'cinema',
    'سينما وإيفيهات',
    2,
    10,
    '+12',
    '25-35 دقيقة',
    'سهل ممتنع',
    'أول لعبة ورقية تشخيصية لعلاج مدمني السينما المصرية وإيفيهات الأفلام!',
    'مصممة على شكل علبة دواء حقيقية وبداخلها روشتة وكروت! أسئلة واختبارات لإيفيهات السينما المصرية الكلاسيكية والحديثة من أيام الأبيض والأسود لحد هنيدي والزعيم وأحمد حلمي.',
    '1. اسحب كارت الروشتة واقرأ الإيفيه أو الموقف السينمائي.
2. باقي اللعيبة لازم يقولوا مين قال الإيفيه، في أنهي فيلم، وسنة كام لو فيه بونص.
3. أسرع واحد بيجاوب بياخد كارت الجرعة ويكسب نقاط التعافي!',
    'الفايز هو أول دكتور سينما يجمع 10 كروت جرعات صحيحة.',
    '/games/kataflam.webp',
    '["سينما", "أفلام", "إيفيهات", "نوستالجيا", "ثقافة عامة", "شلة"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'tasali-aflam',
    'تسالي: أفلام السينما',
    'Tasali Aflam El Cinema',
    'تسالي (2oolameme)',
    'https://2oolameme.com',
    'cinema',
    'سينما وإيفيهات',
    2,
    8,
    '+10',
    '15-20 دقيقة',
    'سهل وممتع',
    'إيفيهات، أسماء أفلام، ومشاهد لا تُنسى في علبة جيب خفيفة!',
    'علبة كروت تسالي سينمائية سريعة للجيب. اختبارات خاطفة لأشهر مشاهد السينما المصرية، من زمان لحد النهاردة، بأقصر وقت وأعلى متعة.',
    '1. اسحب كارت التحدي السينمائي.
2. مثل المشهد أو قل الإيفيه المكتوب بدون ذكر اسم الفيلم.
3. أول واحد يخمن الفيلم ياخد الكارت.',
    'لعبة خفيفة تخلص مع فنجان قهوة تركي مظبوط.',
    '/games/tasali-cinema.webp',
    '["سينما", "تسالي", "أفلام", "سريعة", "ضحك"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'raz3-el-gomhoor',
    'رزع الجمهور (كورة)',
    'Raz3 El Gomhoor',
    'مطور كروي مستقل',
    'https://emadafandi.com',
    'football',
    'كورة ورزع',
    2,
    12,
    '+10',
    '30 دقيقة',
    'متوسط لعشاق الكورة',
    'أهلي وزمالك وتحكيم ورزع.. سهرة كروية نارية على القهوة!',
    'لعبة الرزع الكروي المصرية الأشهر على قهاوي مصر! مقارنات تاريخية بين أساطير الأهلي والزمالك، تحليل لقطات تحكيمية، ومناقشات تثبت مين بيفهم ومين بيهبد في الكورة.',
    '1. اسحب كارت المقارنة الكروية.
2. كل طرف يعرض وجهة نظره والدلائل في دقيقة.
3. باقي الطاولة بتصوت كـ ''جمهور محايد''، وصاحب أعلى حجة ورزع مقنع يكسب الكارت.',
    'ممنوع التعصب، الضحك والروح الرياضية هي أساس القعدة.',
    '/games/raz3-el-gomhoor.webp',
    '["كورة", "رزع", "أهلي وزمالك", "رياضة", "شلة شباب"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'couples-walaken',
    'Couples ولكن',
    'Couples Walaken',
    'JokeyJoy',
    'https://jokeyjoy.com',
    'couples',
    'كابلز وصراحة',
    2,
    2,
    '+18',
    '40 دقيقة',
    'عميق',
    'حب من نوع مختلف.. كلام يقرّب المسافات بجد.',
    'لعبة مخصصة للكابلز والمخطوبين والمتزوجين في كافيه عماد أفندي. أسئلة ذكية ونقاشات ممتعة بتفتح مواضيع في العلاقة وتكتشفوا حاجات جديدة في تفكير بعض.',
    '1. اسحب كارت من القسم المناسب (ذكريات، مشاعر، مستقبل، مواقف طريفة).
2. كل طرف بيجاوب على السؤال بصراحة تامة.
3. كروت التحديات الرومانسية بتضيف روح لطيفة للقعدة.',
    'مفيش فايز وخسران؛ الهدف جلسة حوار دافئة وتفاهم عميق مع فنجان قهوة رايق.',
    '/games/couples-walaken.webp',
    '["كابلز", "مخطوبين", "رومانسية", "حوار", "عميق"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'mawada-w-rahma',
    'مودة ورحمة',
    'Mawada w Rahma',
    'شركة رباط (Rebaat)',
    'https://rebaat.com',
    'couples',
    'كابلز وصراحة',
    2,
    2,
    '+18',
    '45-60 دقيقة',
    'عميق وراقي',
    'جلسة حوار زوجي دافئة.. لبناء بيت سعيد وتفاهم عميق.',
    'من أشهر إصدارات شركة رباط المتخصصة في العلاقات الأسرية. بطاقات حوارية هادفة وممتعة للمتزوجين والمقبلين على الزواج لمناقشة أسس الحياة، التقدير، لغات الحب، والمواقف اليومية في جو راقي مع فنجان قهوة.',
    '1. اسحب كارت من المحاور الأربعة (امتنان، تفاهم، مواقف، مشاعر).
2. كل شريك يشارك بصدق وهدوء.
3. كروت المبادرات العملية بتعطي لمسات لطيفة تقوي المودة بين الزوجين.',
    'مفيش فايز وخسران؛ القعدة هدفها التقارب والونس وبناء الروابط الحقيقية.',
    '/games/mawada-w-rahma.webp',
    '["رباط", "مودة ورحمة", "كابلز", "زواج", "حوار", "عميق"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'qabl-el-hewar',
    'قبل الحوار',
    'Qabl El Hewar',
    'شركة رباط (Rebaat)',
    'https://rebaat.com',
    'couples',
    'كابلز وصراحة',
    2,
    2,
    '+18',
    '40-50 دقيقة',
    'عميق',
    'للمخطوبين والمقبلين على الارتباط.. كسر الجليد وتوافق الأفكار.',
    'إصدار راقي من شركة رباط مخصص لجلسات التعارف والخطوبة والارتباط. بيساعد الطرفين يتعرفوا على طريقة تفكير بعض، طموحات المستقبل، الطباع، والقيم الشخصية بأسلوب لطيف وخالي من التوتر والضغط.',
    '1. سحب كروت الأسئلة الهادئة بالتبادل.
2. الإجابة بتلقائية ومناقشة وجهات النظر بهدوء.
3. كروت التوافق بتحدد نقاط التلاقي الجميلة بين الطرفين.',
    'وسيلة ممتازة ومثالية لأي كابلز في الكافيه يقضوا وقت مفيد وممتع.',
    '/games/qabl-el-hewar.webp',
    '["رباط", "قبل الحوار", "خطوبة", "تعارف", "كابلز", "تفاهم"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'pick-a-date',
    'Pick A Date',
    'Pick A Date',
    'قول أميم (2oolameme)',
    'https://2oolameme.com',
    'couples',
    'كابلز وصراحة',
    2,
    4,
    '+16',
    '30 دقيقة',
    'سهل',
    'الديت المثالي ولا الخروجة الكارثية؟ خطط لخروجتك بدون نكد!',
    'لعبة خفيفة ممتعة عن سيناريوهات الديتس والمواعيد والخروجات في مصر! كروت بتعرض مواقف مضحكة، كوارث طلبات المنيو، مواقف التأخير، واللحظات المحرجة.',
    '1. اسحب كارت سيناريو الخروجة.
2. قارن الحلول والردود المقترحة.
3. قيم الديت وشوف مين هيعرف ينقذ الخروجة من النكد.',
    'مثالية للكابلز والأصحاب المقربين لكسر الروتين والضحك.',
    '/games/pick-a-date.webp',
    '["ديت", "خروجات", "كابلز", "ضحك", "مواقف"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'girls-walaken',
    'Girls ولكن',
    'Girls Walaken',
    'JokeyJoy',
    'https://jokeyjoy.com',
    'girls',
    'بنات فقط',
    3,
    8,
    '+17',
    '45 دقيقة',
    'سهل',
    'لعبة ورقية للبنات فقط.. أسرار وسوالف بدون فلاتر!',
    'أشهر لعبة مخصصة لقعدات البنات في الكافيه! كروت مواقف، قصف جبهات، اعترافات، وسيناريوهات عن العلاقات، الفاشون، المواقف المحرجة، والصحاب.',
    '1. سحب كروت بالترتيب بين البنات.
2. كل كارت بيطرح سؤال صريح أو مقارنة أو اختيار صعب.
3. التصويت والتفاعل هو اللي بيحدد مين صاحبة أكتر قصف جبهة في الجولة.',
    'ممنوع دخول الشباب في اللعبة نهائياً! خصوصية كاملة وضحك بدون حواجز.',
    '/games/girls-walaken.webp',
    '["بنات", "أسرار", "صراحة", "سوالف", "سهرة بنات"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'waraa-el-gareema',
    'وراء الجريمة: فندق الدم',
    'Waraa El Gareema - Fondok El Dam',
    'Handa Games',
    'https://handagames.com',
    'mystery',
    'تحقيقات وجرائم',
    2,
    8,
    '+16',
    '60-90 دقيقة',
    'متقدم وذكي',
    'لعبة تحقيق في جريمة كاملة من Handa Games.. بس مفيش مجرم مبيسبش وراه خيط!',
    'ملف قضية حقيقي كامل ومستقل عن مسرح الجريمة من إنتاج Handa Games. يحتوي على تقارير الطب الشرعي، شهادات الشهود، صور مسرح الجريمة داخل الفندق، وأدلة جنائية للوصول للجاني.',
    '1. افتح ملف القضية واقرأ بيان البداية.
2. وزع الأدلة والصور وتقارير المعمل الجنائي بين أفراد الطاولة.
3. قارنوا الأوقات وحجج الغياب واستبعدوا المشتبه بهم حتى كشف القاتل والدافع.',
    'تحتاج تركيز عالي ومناقشة تفاعلية ممتعة جداً تستمر لأكتر من ساعة.',
    '/games/waraa-el-gareema.webp',
    '["تحقيق", "غموض", "هاندا", "جريمة", "ذكاء", "سهرة طويلة"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'khufu',
    'خوفو (Khufu)',
    'Khufu Escape',
    'Meego Studios',
    'https://meegostudios.com',
    'mystery',
    'تحقيقات وجرائم',
    2,
    6,
    '+8',
    '20 دقيقة',
    'سهل وحماسي',
    'المستكشف والمومياوات.. اهرب من المقبرة قبل ما تتقفل عليك!',
    'لعبة مغامرات وسرعة رد فعل ممتعة جداً من Meego Studios! المستكشف الصغير بيحاول يهرب من لعنة الفراعنة والمومياوات بجمع المفاتيح وتفادي الفخاخ.',
    '1. اقلب كروت المقبرة بسرعة على الطاولة.
2. طابق الرموز الهيروغليفية ومسارات الهروب قبل ما المومياء تظهر.
3. أول لاعب يجمع 3 تمائم ذهبية يهرب من الهرم ويفوز.',
    'سرعة عينك ويدك هي اللي هتنقذك من المومياوات.',
    '/games/khufu.webp',
    '["خوفو", "ميجو", "مغامرة", "سرعة", "عائلي", "فراعنة"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'mansa',
    'مانسا (MANSA)',
    'Mansa',
    'MANSA Games',
    'https://mansagames.com',
    'strategy',
    'استثمار وتخطيط',
    3,
    6,
    '+12',
    '40-50 دقيقة',
    'متوسط وذكي',
    'إمبراطورية الذهب والثروة.. العبها بذكاء مانسا موسى!',
    'لعبة التداول والاستثمار المالي المستوحاة من أسطورة أغنى رجل في التاريخ (مانسا موسى). كروت الذهب والجمال والقوافل التجارية وبناء القصور والسيطرة على أسواق التجارة.',
    '1. كل لاعب بيبدأ برأس مال من سبائك الذهب وقوافل التجارة.
2. بتتحرك في الأسواق وتشتري الموارد وتضارب على الأسعار.
3. استغل كروت الأحداث الاقتصادية لزيادة أرباحك وإفلاس منافسيك.
4. اللي يجمع أكبر ثروة ذهبية في نهاية الجولات هو إمبراطور مانسا.',
    'الذكاء المالي والتفاوض مع باقي اللاعبين هو مفتاح الفوز.',
    '/games/mansa.webp',
    '["مانسا", "ذهب", "تجارة", "استثمار", "ذكاء", "سهرة طويلة"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'kelmet-el-ser-mostathmer',
    'كلمة السر: مستثمر',
    'Mostathmer - ONE Games',
    'ONE Games',
    'https://onegameseg.com',
    'strategy',
    'استثمار وتخطيط',
    2,
    6,
    '+12',
    '30-40 دقيقة',
    'متوسط',
    'فك الشفرة واستثمر صح.. صفقات وشركات وبورصة على القهوة!',
    'لعبة ورقية استراتيجية مالية من ONE Games. بتدمج بين سرعة فك الشفرات والكلمات السرية وتوجيه الاستثمارات والأسهم في الشركات الناشئة وتفادي الأزمات المالية.',
    '1. كروت شركات وقطاعات استثمارية مكشوفة على الطاولة.
2. كروت كلمة السر بتعطي تلميحات ذكية للصفقة الرابحة.
3. أسرع لاعب يستنتج الشفرة يقتنص الصفقة ويوسع محفظته الاستثمارية.',
    'اجمع محفظة متوازنة من الأصول وتجنب كروت التضخم والإفلاس.',
    '/games/kelmet-el-ser-mostathmer.webp',
    '["مستثمر", "بزنس", "ذكاء", "كلمة السر", "استثمار", "تحدي"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'tomouhy',
    'طموحي (Tomouhy)',
    'Tomouhy',
    'شركة ألعاب فكرية مصرية',
    'https://emadafandi.com',
    'strategy',
    'استثمار وتخطيط',
    2,
    6,
    '+10',
    '35-45 دقيقة',
    'متوسط',
    'خطط لمستقبلك وحقق أهدافك الكبيرة خطوة بخطوة!',
    'لعبة لوحية وكروت عائلية وتنافسية حول مسارات الحياة والمهن وتحقيق الطموحات. بتبدأ من الصفر، وتواجه قرارات حاسمة (دراسة، استثمار، سفر، مشاريع) وتوازن بين الشغف والمال لتحقيق طموحك الأول.',
    '1. اختار بطاقة مسار الطموح.
2. حرك مجسمك على لوحة الأحداث والفرص.
3. وظف مواردك بحكمة للتغلب على التحديات وجمع نقاط النجاح.',
    'أول لاعب يكمل شروط طموحه الرئيسي يفوز بالجولة.',
    '/games/tomouhy.webp',
    '["طموحي", "لوحية", "أهداف", "تخطيط", "عائلي", "شباب"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'skrew-pocket',
    'سكرو (نسخة الجيب)',
    'SKREW Pocket',
    'YAMP Store',
    'https://sllr.co/yampstore',
    'quick',
    'كروت وتسالي سريعة',
    2,
    6,
    '+8',
    '20 دقيقة',
    'سهل وممتع',
    'لعبة الكروت التريند رقم 1 في مصر.. سكرو واقلب الطاولة!',
    'لعبة الورق الأكثر انتشاراً وشعبية في كافيهات مصر! تعتمد على الذاكرة السريعة وقدرات الكروت الخاصة (بص في كارت، بدل مع خصمك، اسحب 2) بهدف تقليل مجموع كروتك لأقل رقم ممكن.',
    '1. كل لاعب معاه 4 كروت مقلوبة ومسموح له يشوف 2 منهم بس في الأول.
2. في دورك بتسحب كارت من الأرض وتقرر تبدله ولا ترميه وتستخدم قدرته.
3. لما تحس إن مجموع كروتك هو الأقل في الطاولة بتصرخ: ''سكرو!'' وتنتهي الجولة.',
    'أقل مجموع نقاط هو الفائز، واللي يقول سكرو ويطلع غلط بيلبس ضعف النقط!',
    '/games/skrew.webp',
    '["كروت", "ذاكرة", "تريند", "حماس", "سريعة", "إدمان"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'autobeez-complete-cards',
    'أتوبيس كومبليت (كروت)',
    'Autobeez Complete Cards',
    'Duckling',
    'https://ducklingeg.com',
    'quick',
    'كروت وتسالي سريعة',
    2,
    8,
    '+8',
    '15 دقيقة',
    'سهل وممتع',
    'ولد، بنت، جماد، بلاد.. الكلاسيكية المصرية في ثوب كروت خاطف!',
    'التحول العصري للعبة القلم والورقة التاريخية ''أتوبيس كومبليت'' من Duckling! كروت حروف وتصنيفات سريعة، ومين هيجمع الكلمات ويصرخ ''أتوبيس كومبليت!'' الأول.',
    '1. كارت تصنيف مكشوف في النص (نبات، حيوان، بلاد، مشاهير).
2. كارت حرف بيتقلب فجأة.
3. أول واحد ينطق كلمة صحيحة بتبدأ بالحرف في التصنيف ياخد الكارت.',
    'الفايز هو أول واحد يجمع 10 كروت أتوبيس كومبليت.',
    '/games/autobeez.webp',
    '["أتوبيس كومبليت", "داكلينج", "سرعة", "نوستالجيا", "عائلي"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'sahseh',
    'صحصح!',
    'Sahseh',
    'Saleeny',
    'https://saleenyeg.com',
    'quick',
    'كروت وتسالي سريعة',
    2,
    6,
    '+8',
    '15 دقيقة',
    'سهل جداً',
    'عينك في وسط راسك.. أول واحد يلمح الرابط يكسب!',
    'لعبة تركيز وسرعة ملاحظة خاطفة على غرار دوبل ولكن بطابع ورسومات مصرية مبهجة من ساليني. دايماً فيه عنصر واحد مشترك بين أي كارتين، ومهمتك تصرخ بيه الأول!',
    '1. كارت مكشوف في النص وكارت مع كل لاعب.
2. ابحث بسرعة عن الرمز المشترك بين كارتك وكارت الأرض.
3. أول واحد ينطق الرمز يحط كروته في النص، والفايز هو اللي يخلص ورقه الأول.',
    'تناسب الأطفال والشباب والكبار، وتنعش الدماغ مع رشفة قهوة.',
    '/games/sahseh.webp',
    '["تركيز", "ملاحظة", "سرعة", "ساليني", "أطفال وعائلات"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    '3arosty',
    'عروستي!',
    '3arosty',
    'W2P Games',
    'https://w2pgames.com',
    'quick',
    'كروت وتسالي سريعة',
    2,
    8,
    '+8',
    '20 دقيقة',
    'سهل',
    'الفزورة المصرية التاريخية.. معاك 20 سؤال تعرفها؟',
    'اللعبة الشعبية الأصيلة عروستي في ثوب ورقي أنيق من W2P Games! لاعب يسحب كارت الشيء السري وباقي القعدة يسألوه أسئلة إجابتها ''أه'' أو ''لا'' بس لحد ما يخمنوها.',
    '1. اسحب كارت بدون ما حد يشوفه.
2. كل لاعب في دوره بيسأل سؤال محدد (بيتاكل؟ في البيت؟ مصنوع من خشب؟).
3. صاحب الكارت يجاوب بـ أه أو لأ.
4. اللي يخمن ''عروستي'' صح ياخد الكارت ويكسب نقطة.',
    'ممنوع ذكر الكلمة صراحة أو إعطاء تلميحات خارج نطاق نعم ولا.',
    '/games/3arosty.webp',
    '["فوازير", "ذكاء", "أسئلة", "كلاسيك", "عائلي"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'tasali-kelma-fe-serrak',
    'تسالي: كلمة في سرك',
    'Tasali - Kelma Fe Serrak',
    'تسالي (2oolameme)',
    'https://2oolameme.com',
    'quick',
    'كروت وتسالي سريعة',
    2,
    8,
    '+10',
    '15 دقيقة',
    'سهل',
    'همس وسرعة تخمين.. كلمة واحدة تغير معنى الجملة كلها!',
    'علبة تسالي سريعة للجيب تعتمد على الهمس والتلميح السريع بين أفراد الفريق لتخمين الكلمة السرية في أسرع وقت.',
    '1. اسحب كارت الكلمة السرية.
2. أعطِ تلميحاً من كلمة واحدة فقط لزميلك.
3. لو خمنها صح في أول محاولة تكسبوا الكارت.',
    'ممنوع ذكر أي جزء من الكلمة الأصلية أو استخدام حركات اليدين.',
    '/games/tasali-kelma-khatar.webp',
    '["تسالي", "همس", "سرعة", "تلميح", "شلة"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'tasali-3andalib',
    'تسالي: عندليب الأحبة',
    'Tasali - 3andalib El A7ebba',
    'تسالي (2oolameme)',
    'https://2oolameme.com',
    'quick',
    'كروت وتسالي سريعة',
    2,
    8,
    '+10',
    '15 دقيقة',
    'سهل وممتع',
    'طرب وأغاني وزمن الفن الجميل.. دندن وكمل الكوبليه!',
    'لعبة التسالي الموسيقية والغنائية لرواد الكافيه! مقتطفات من أشهر أغاني عبد الحليم، أم كلثوم، منير، والهضبة، ومطلوب تكملة الكوبليه أو دندنة اللحن.',
    '1. اسحب كارت الأغنية واقرأ المقطع الأول.
2. باقي الطاولة يتنافسوا على تكملة الكوبليه بشكل صحيح.
3. صاحب أحسن صوت أو أسرع إجابة ياخد الكارت.',
    'جو طربي وضحك مبهج على الطاولة.',
    '/games/tasali-3andalib.webp',
    '["تسالي", "أغاني", "طرب", "دندنة", "نوستالجيا"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'tasali-haqeeqa-khayal',
    'تسالي: حقيقة ولا خيال؟',
    'Tasali - Haqeeqa Wala Khayal',
    'تسالي (2oolameme)',
    'https://2oolameme.com',
    'quick',
    'كروت وتسالي سريعة',
    2,
    8,
    '+10',
    '15 دقيقة',
    'سهل',
    'معلومة صادمة بجد ولا مقلب متفبرك؟ صدق أو لا تصدق!',
    'كروت تسالي سريعة بتطرح حقائق علمية وتاريخية وغريبة جداً، ومهمة الطاولة التخمين: هل المعلومة دي حقيقة حقيقية ولا خيال ومقلب متألف!',
    '1. اسحب الكارت واقرأ المعلومة الصادمة.
2. كل لاعب يصوت بـ ''حقيقة'' أو ''خيال''.
3. اكشف ظهر الكارت لتعرف الحقيقة والصدمة العلمية!',
    'الفايز هو أكتر واحد يميز الحقائق من الأساطير.',
    '/games/tasali-haqeeqa.webp',
    '["تسالي", "حقائق", "صدمة", "معلومات", "سريعة"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'tasali-system',
    'تسالي: سيستم',
    'Tasali - System',
    'تسالي (2oolameme)',
    'https://2oolameme.com',
    'quick',
    'كروت وتسالي سريعة',
    2,
    8,
    '+10',
    '15 دقيقة',
    'سهل',
    'السيستم واقع ولا شغال؟ سرعة ترتيب وتركيز خاطف!',
    'لعبة كروت تسالي تعتمد على القواعد المتغيرة والمفاجئة في كل جولة، حيث يفرض ''السيستم'' شرطاً جديداً يجب على الجميع اتباعه فوراً.',
    '1. اكشف كارت السيستم الجديد.
2. اتبع التعليمات السريعة (تحدث بدون حرف معين، لا تنظر لعين خصمك).
3. أول من يخترق السيستم يعاقب فوراً.',
    'الالتزام بقواعد السيستم هو طريق النجاة.',
    '/games/tasali-system.webp',
    '["تسالي", "سيستم", "تركيز", "سرعة", "ضحك"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'tasali-kalam-fady',
    'تسالي: كلام فاضي',
    'Tasali - Kalam Fady',
    'تسالي (2oolameme)',
    'https://2oolameme.com',
    'quick',
    'كروت وتسالي سريعة',
    2,
    8,
    '+10',
    '15 دقيقة',
    'سهل جداً',
    'رغي وهبد وضحك على الفاضي.. مين يعرف يرغي دقيقة بدون ما يتلخبط؟',
    'تحدي الكلام والارتجال السريع! كروت بتفرض مواضيع عبثية تافهة وتطلب من اللاعب التحدث عنها بجدية لمدة دقيقة كاملة بدون تردد أو ضحك.',
    '1. اسحب كارت الموضوع العبثي.
2. شغل تايمر 60 ثانية.
3. اتكلم بجدية مقنعة واكسب تصفيق وضحك القعدة كلها.',
    'لو سكت أكتر من ثانيتين أو ضحكت تخسر الجولة.',
    '/games/tasali-dehk.webp',
    '["تسالي", "رغي", "هبد", "ضحك", "ارتجال"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'tasali-madfa3-ramadan',
    'تسالي: مدفع رمضان',
    'Tasali - Madfa3 Ramadan',
    'تسالي (2oolameme)',
    'https://2oolameme.com',
    'quick',
    'كروت وتسالي سريعة',
    2,
    8,
    '+8',
    '15 دقيقة',
    'سهل ومبهج',
    'مدفع الإفطار اضرب! أجواء رمضانية ونوستالجيا الفوازير والمسلسلات.',
    'كروت تسالي رمضانية بامتياز! فوازير فطوطة وشريهان، ذكريات بوجي وطمطم، وأشهر مسلسلات وأكلات رمضان في مصر.',
    '1. اسحب كارت الفزورة الرمضانية.
2. اقرأ التلميحات بالتدريج.
3. أسرع من يحل الفزورة قبل دقة المدفع يكسب الكارت.',
    'مثالية لسهرات رمضان والأعياد في كافيه عماد أفندي.',
    '/games/tasali-ramadan.webp',
    '["رمضان", "فوازير", "تسالي", "نوستالجيا", "عائلي"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'starting-chess',
    'شطرنج البداية (Starting Chess)',
    'Starting Chess',
    'ألعاب الذكاء الكلاسيكية',
    'https://emadafandi.com',
    'classic',
    'كلاسيك ومسابقات',
    2,
    2,
    '+6',
    '20-45 دقيقة',
    'استراتيجي راقي',
    'ملك الألعاب الذهنية.. خطط، هاجم، وكش ملك!',
    'طقم الشطرنج الكلاسيكي التعليمي المتوفر في الكافيه. مثالي لعشاق التفكير العميق والتكتيك مع فنجان إسبريسو كولومبي هادئ.',
    'القواعد الدولية الكلاسيكية للشطرنج، مع قطع واضحة وسهلة الحركة للمبتدئين والمحترفين.',
    'كش ملك ينهي اللعبة، وتكتيك افتتاحيات الشطرنج هو الأساس.',
    '/games/starting-chess.webp',
    '["شطرنج", "ذكاء", "كلاسيك", "استراتيجية", "تركيز"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'original-domino',
    'دومينو أصلي (Original Domino)',
    'Original Domino',
    'دومينو القهاوي الكلاسيكي',
    'https://emadafandi.com',
    'classic',
    'كلاسيك ومسابقات',
    2,
    4,
    '+8',
    '15-30 دقيقة',
    'سهل وتكتيكي',
    'أساس قعدة القهوة المصرية.. سد ولعب وقفلة معلم!',
    'طقم الدومينو الأصلي (عاجي أسود وأبيض فاخر) بروح القهوة المصرية الأصيلة. العب ألعاب الدومينو المتنوعة: العادي، القفلة، أو الأمريكاني.',
    'توزيع 7 قطع لكل لاعب ومطابقة الأرقام المتشابهة، وتخطيط القفلة لحبس الخصم والفوز بنقاط الطاولة.',
    'الفايز من يفرغ قطعه أولاً، أو صاحب أقل مجموع نقاط عند القفلة.',
    '/games/original-domino.webp',
    '["دومينو", "قهوة", "كلاسيك", "شعبي", "سد"]'
);
INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    'mawsoo3at-al-ma3refa',
    'سلسلة بطاقات المعرفة والمسابقات (16 جزء)',
    'Knowledge & Trivia Cards Series',
    'دار المعرفة الثقافية',
    'https://emadafandi.com',
    'classic',
    'كلاسيك ومسابقات',
    2,
    10,
    '+8',
    '15-25 دقيقة',
    'ثقافي مشوق',
    '16 علبة معلومات ومسابقات.. السيرة النبوية، القرآن، الفضاء، والغرائب!',
    'الرف الثقافي الكامل في كافيه عماد أفندي: السيرة النبوية، صحابة الرسول، قصص القرآن، ألغاز وأحاجي، معلومات عامة، عجائب الدنيا، اختراعات، الفضاء والكون، كوكب الأرض، وعجائب العلوم والحيوانات. أسئلة سريعة ممتعة جداً للتحدي الثقافي.',
    'سحب بطاقات الأسئلة والتنافس الفردي أو الجماعي على سرعة ودقة الإجابة وجمع بطاقات التميز.',
    'أعلى رصيد بطاقات صحيحة يتوج بلقب مثقف الجلسة.',
    '/games/mawsoo3at.webp',
    '["ثقافة", "سيرة نبوية", "معلومات عامة", "مسابقات", "عائلي", "ذكاء"]'
);