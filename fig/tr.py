
import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    # 電源レール（上）
    vcc = d.add(elm.SourceV().label('$V_{CC}$').up())
    d.add(elm.Line().right().length(3))
    d.add(elm.Dot(open=True).label('$v_{out}$', 'right'))

    # コレクタ抵抗 RC（下向き）
    d.push()  # レールの中点を保存
    d.add(elm.Line().left().length(1.5))
    d.add(elm.Resistor().down().label('$R_C$'))
    # NPNトランジスタ
    q1 = d.add(elm.BjtNpn().anchor('c').right())
    # エミッタ抵抗 RE → GND
    d.add(elm.Resistor().down().label('$R_E$'))
    d.add(elm.Ground())

    # ベース側：RB と vin
    d.pop()  # レールの中点へ戻る
    d.add(elm.Line().down().length(1.5))
    d.add(elm.Line().left().length(2))
    d.add(elm.Resistor().left().label('$R_B$'))
    src = d.add(elm.SourceSin().down().label('$v_{in}$'))
    d.add(elm.Line().down().length(0.5))
    d.add(elm.Ground())

    # ラベル
    q1.label('$Q_1$ (NPN)', 'right')

    d.save('common_emitter.png')  # or .svg / .pdf
