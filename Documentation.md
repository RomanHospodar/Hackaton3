Projektová documentace

Zadání:
Klasifikujte pomocí modelu vstupní satelitní snímky do jedné ze dvou tříd:
- Má solární panel
- Nemá solární panel

Jak na to:
Snažil jsem se využít předškolené Keras modely na imagenet a jemným laděním je přizpůsobit pro naše zadání.

Popis trénování modelu:
Začal jsem tím, že jsem importoval nezbytné knihovny, jako byly TensorFlow, Keras a další.
Definoval jsem cesty k tréninkovým a validačním datovým sadám obrázků, určil jsem rozměry obrázků a velikost dávky pro zpracování.
Vytvořil jsem generátory dat pro tréninkovou a validační sadu dat pomocí funkce image_dataset_from_directory v TensorFlow.
Zkoušel jsem různé předškolené modely jako například ResNet50, ResNet152, Xception, ConvNeXtXLarge.
Pro extrakci rysů nejlépe vycházel předškolený model ConvNeXtXLarge.
Zafixoval jsem jeho vrstvy, abych zabránil dalšímu tréninku.
Definoval jsem několik parametrů pro ladění hyperparametrů, včetně hodnot pro vynechávání (dropout), funkce ztráty, aktivační funkce a další.
Pomocí smyček jsem zkoušel různé kombinace hyperparametrů a trénoval několik modelů, každý s různými nastaveními.
Pro rychlejší trénink jsem používal možnost trénování pomocí GPU.
Trénoval jsem modely po určený počet epoch a pak jemně ladil model tím, že jsem umožnil (tentokrát všem) vrstvám  
základního modelu být trénovatelnými s různými hodnotami learning rate.
Následně jsem ukládal nejlepší model na základě výkonnosti na validačních datech.
Nejlepší model jsem poté použil pro predikci testovacích obrázků.
A noc jsem strávil tím, jak to celé dostat na GitHub, aby to fungovalo - nejtěžší krok celé úlohy :-)