#!/usr/bin/env python3
"""
V3: Premium wireframe topology SVG - female front view.
Fashion-model proportions, organic polygon flow, beauty-tech aesthetic.
Designed for AI beauty measurement platform context.
"""

vertices = []
polygons = []

def v(x, y):
    vertices.append((round(x, 1), round(y, 1)))
    return len(vertices) - 1

def poly(indices, region):
    polygons.append((indices, region))

# ============================================================
# FEMALE FRONT VIEW - PREMIUM A-POSE
# ViewBox: 0 0 800 1200
# Center: x=400
# Fashion proportions: ~8.5 head heights, elongated legs
# Head height ~100px, total ~1100px
# ============================================================

# ---- CROWN ----
c0 = v(400, 22)     # crown apex
c1 = v(382, 28)     # crown left
c2 = v(418, 28)     # crown right
c3 = v(370, 38)     # upper skull left
c4 = v(400, 34)     # crown center
c5 = v(430, 38)     # upper skull right

# ---- FOREHEAD ----
f0 = v(364, 52)     # forehead outer left
f1 = v(384, 48)     # forehead inner left
f2 = v(400, 46)     # forehead center
f3 = v(416, 48)     # forehead inner right
f4 = v(436, 52)     # forehead outer right

# ---- TEMPLE / BROW ----
t0 = v(358, 66)     # temple left
t1 = v(374, 64)     # brow outer left
t2 = v(388, 66)     # brow mid left
t3 = v(400, 64)     # glabella
t4 = v(412, 66)     # brow mid right
t5 = v(426, 64)     # brow outer right
t6 = v(442, 66)     # temple right

# ---- EYES ----
e0 = v(360, 76)     # outer canthus left
e1 = v(372, 73)     # upper lid left
e2 = v(384, 75)     # inner canthus left
e3 = v(400, 74)     # nose bridge
e4 = v(416, 75)     # inner canthus right
e5 = v(428, 73)     # upper lid right
e6 = v(440, 76)     # outer canthus right
e7 = v(370, 82)     # lower lid left
e8 = v(430, 82)     # lower lid right

# ---- NOSE ----
n0 = v(400, 82)     # nose bridge lower
n1 = v(394, 92)     # nose left
n2 = v(400, 95)     # nose tip
n3 = v(406, 92)     # nose right

# ---- CHEEKS ----
k0 = v(356, 86)     # zygomatic left
k1 = v(444, 86)     # zygomatic right
k2 = v(354, 100)    # mid cheek left
k3 = v(446, 100)    # mid cheek right

# ---- MOUTH ----
m0 = v(386, 104)    # mouth corner left
m1 = v(400, 102)    # philtrum
m2 = v(414, 104)    # mouth corner right
m3 = v(392, 110)    # lower lip left
m4 = v(400, 112)    # lower lip center
m5 = v(408, 110)    # lower lip right

# ---- JAW ----
j0 = v(356, 112)    # jaw angle left
j1 = v(444, 112)    # jaw angle right
j2 = v(362, 124)    # lower jaw left
j3 = v(438, 124)    # lower jaw right
j4 = v(374, 134)    # chin side left
j5 = v(400, 138)    # chin point
j6 = v(426, 134)    # chin side right

# ---- NECK ----
nk0 = v(378, 148)   # neck left
nk1 = v(400, 146)   # neck center
nk2 = v(422, 148)   # neck right
nk3 = v(374, 162)   # neck mid left
nk4 = v(400, 160)   # neck mid center
nk5 = v(426, 162)   # neck mid right
nk6 = v(370, 176)   # neck base left
nk7 = v(400, 174)   # neck base center
nk8 = v(430, 176)   # neck base right

# ---- SHOULDER SHELF ----
s0 = v(340, 182)    # inner shoulder left
s1 = v(460, 182)    # inner shoulder right
s2 = v(302, 188)    # shoulder point left
s3 = v(498, 188)    # shoulder point right
s4 = v(268, 198)    # deltoid apex left
s5 = v(532, 198)    # deltoid apex right
s6 = v(252, 216)    # deltoid outer left
s7 = v(548, 216)    # deltoid outer right

# ---- COLLARBONE ----
cb0 = v(354, 184)   # clavicle inner left
cb1 = v(400, 180)   # suprasternal notch
cb2 = v(446, 184)   # clavicle inner right

# ---- UPPER CHEST ----
ch0 = v(344, 202)   # chest outer left
ch1 = v(372, 196)   # chest inner left
ch2 = v(400, 194)   # sternum top
ch3 = v(428, 196)   # chest inner right
ch4 = v(456, 202)   # chest outer right

# ---- BUST LINE ----
b0 = v(338, 222)    # bust outer left
b1 = v(366, 218)    # bust peak left
b2 = v(400, 214)    # sternum mid
b3 = v(434, 218)    # bust peak right
b4 = v(462, 222)    # bust outer right

# ---- UNDER BUST ----
ub0 = v(334, 244)   # underbust outer left
ub1 = v(364, 238)   # underbust inner left
ub2 = v(400, 236)   # solar plexus
ub3 = v(436, 238)   # underbust inner right
ub4 = v(466, 244)   # underbust outer right

# ---- RIBCAGE ----
r0 = v(330, 268)    # rib outer left
r1 = v(362, 262)    # rib inner left
r2 = v(400, 260)    # xiphoid
r3 = v(438, 262)    # rib inner right
r4 = v(470, 268)    # rib outer right

# ---- WAIST (narrowest) ----
w0 = v(334, 296)    # waist outer left
w1 = v(364, 290)    # waist inner left
w2 = v(400, 288)    # navel
w3 = v(436, 290)    # waist inner right
w4 = v(466, 296)    # waist outer right

# ---- LOWER ABDOMEN ----
la0 = v(332, 324)   # lower abd outer left
la1 = v(364, 318)   # lower abd inner left
la2 = v(400, 316)   # lower abd center
la3 = v(436, 318)   # lower abd inner right
la4 = v(468, 324)   # lower abd outer right

# ---- ILIAC / HIP BONE ----
h0 = v(324, 352)    # iliac crest left
h1 = v(358, 346)    # hip inner left
h2 = v(400, 342)    # pubic center
h3 = v(442, 346)    # hip inner right
h4 = v(476, 352)    # iliac crest right

# ---- LOWER HIP ----
lh0 = v(318, 378)   # hip outer left
lh1 = v(354, 370)   # hip inner left
lh2 = v(400, 366)   # pubic lower
lh3 = v(446, 370)   # hip inner right
lh4 = v(482, 378)   # hip outer right

# ---- GROIN SPLIT ----
g0 = v(314, 402)    # groin outer left
g1 = v(350, 394)    # groin inner left
g2 = v(400, 390)    # perineum
g3 = v(450, 394)    # groin inner right
g4 = v(486, 402)    # groin outer right
g5 = v(362, 414)    # inner thigh top left
g6 = v(400, 418)    # crotch nadir
g7 = v(438, 414)    # inner thigh top right

# ============================================================
# LEFT ARM - elegant A-pose ~40° angle
# ============================================================
# Upper arm
lua0 = v(242, 232)  # outer deltoid-bicep
lua1 = v(264, 226)  # inner deltoid-bicep
lua2 = v(226, 256)  # outer mid-bicep
lua3 = v(248, 250)  # inner mid-bicep
lua4 = v(212, 280)  # outer low-bicep
lua5 = v(234, 274)  # inner low-bicep
lua6 = v(198, 304)  # outer pre-elbow
lua7 = v(220, 298)  # inner pre-elbow

# Elbow
le0 = v(188, 322)   # elbow outer
le1 = v(210, 316)   # elbow inner
le2 = v(196, 330)   # olecranon

# Forearm
lfa0 = v(182, 346)  # outer upper forearm
lfa1 = v(204, 340)  # inner upper forearm
lfa2 = v(174, 372)  # outer mid forearm
lfa3 = v(196, 366)  # inner mid forearm
lfa4 = v(166, 398)  # outer low forearm
lfa5 = v(188, 392)  # inner low forearm
lfa6 = v(160, 420)  # wrist outer
lfa7 = v(180, 414)  # wrist inner

# Hand
lh_0 = v(156, 434)  # palm heel outer
lh_1 = v(174, 428)  # palm heel inner
lh_2 = v(164, 440)  # palm center
lh_3 = v(150, 446)  # palm outer edge
lh_4 = v(176, 442)  # palm inner edge
lh_5 = v(158, 454)  # palm base

# Thumb
lt0 = v(148, 440)   # thumb base
lt1 = v(142, 448)   # thumb mid
lt2 = v(138, 458)   # thumb tip

# Fingers
lf0 = v(148, 462)   # index base
lf1 = v(144, 472)   # index tip
lf2 = v(156, 466)   # middle base
lf3 = v(152, 478)   # middle tip
lf4 = v(164, 464)   # ring base
lf5 = v(162, 476)   # ring tip
lf6 = v(172, 458)   # pinky base
lf7 = v(172, 468)   # pinky tip

# ============================================================
# RIGHT ARM (mirror)
# ============================================================
rua0 = v(558, 232)
rua1 = v(536, 226)
rua2 = v(574, 256)
rua3 = v(552, 250)
rua4 = v(588, 280)
rua5 = v(566, 274)
rua6 = v(602, 304)
rua7 = v(580, 298)

re0 = v(612, 322)
re1 = v(590, 316)
re2 = v(604, 330)

rfa0 = v(618, 346)
rfa1 = v(596, 340)
rfa2 = v(626, 372)
rfa3 = v(604, 366)
rfa4 = v(634, 398)
rfa5 = v(612, 392)
rfa6 = v(640, 420)
rfa7 = v(620, 414)

rh_0 = v(644, 434)
rh_1 = v(626, 428)
rh_2 = v(636, 440)
rh_3 = v(650, 446)
rh_4 = v(624, 442)
rh_5 = v(642, 454)

rt0 = v(652, 440)
rt1 = v(658, 448)
rt2 = v(662, 458)

rf0 = v(652, 462)
rf1 = v(656, 472)
rf2 = v(644, 466)
rf3 = v(648, 478)
rf4 = v(636, 464)
rf5 = v(638, 476)
rf6 = v(628, 458)
rf7 = v(628, 468)

# ============================================================
# LEFT LEG - elongated fashion proportions
# ============================================================
# Upper thigh
lth0 = v(310, 420)  # outer thigh top
lth1 = v(340, 412)  # front thigh top
lth2 = v(308, 450)  # outer thigh 2
lth3 = v(336, 442)  # front thigh 2
lth4 = v(358, 436)  # inner thigh 2
lth5 = v(304, 484)  # outer thigh 3
lth6 = v(332, 476)  # front thigh 3
lth7 = v(356, 470)  # inner thigh 3
lth8 = v(300, 520)  # outer thigh 4
lth9 = v(328, 512)  # front thigh 4
lth10 = v(354, 506) # inner thigh 4

# Knee
lk0 = v(298, 552)   # knee outer
lk1 = v(324, 546)   # kneecap
lk2 = v(350, 542)   # knee inner
lk3 = v(312, 564)   # below knee center
lk4 = v(296, 568)   # below knee outer
lk5 = v(346, 560)   # below knee inner

# Shin
ls0 = v(296, 590)   # shin outer 1
ls1 = v(316, 584)   # shin front 1
ls2 = v(340, 586)   # shin inner 1
ls3 = v(298, 620)   # shin outer 2
ls4 = v(316, 614)   # shin front 2
ls5 = v(336, 616)   # shin inner 2
ls6 = v(300, 654)   # shin outer 3
ls7 = v(316, 648)   # shin front 3
ls8 = v(334, 650)   # shin inner 3
ls9 = v(302, 688)   # shin outer 4
ls10 = v(316, 682)  # shin front 4
ls11 = v(332, 684)  # shin inner 4

# Ankle
la_0 = v(304, 714)  # ankle outer
la_1 = v(316, 708)  # ankle front
la_2 = v(330, 710)  # ankle inner

# Foot
ft0 = v(300, 728)   # heel outer
ft1 = v(316, 724)   # heel center
ft2 = v(332, 726)   # heel inner
ft3 = v(294, 744)   # midfoot outer
ft4 = v(314, 740)   # midfoot center
ft5 = v(334, 742)   # midfoot inner
ft6 = v(288, 758)   # ball outer
ft7 = v(308, 756)   # ball center
ft8 = v(330, 758)   # ball inner
# Toes
ft9 = v(286, 770)   # big toe
ft10 = v(296, 774)  # 2nd toe
ft11 = v(306, 776)  # 3rd toe
ft12 = v(316, 774)  # 4th toe
ft13 = v(328, 770)  # 5th toe

# ============================================================
# RIGHT LEG (mirror)
# ============================================================
rth0 = v(490, 420)
rth1 = v(460, 412)
rth2 = v(492, 450)
rth3 = v(464, 442)
rth4 = v(442, 436)
rth5 = v(496, 484)
rth6 = v(468, 476)
rth7 = v(444, 470)
rth8 = v(500, 520)
rth9 = v(472, 512)
rth10 = v(446, 506)

rk0 = v(502, 552)
rk1 = v(476, 546)
rk2 = v(450, 542)
rk3 = v(488, 564)
rk4 = v(504, 568)
rk5 = v(454, 560)

rs0 = v(504, 590)
rs1 = v(484, 584)
rs2 = v(460, 586)
rs3 = v(502, 620)
rs4 = v(484, 614)
rs5 = v(464, 616)
rs6 = v(500, 654)
rs7 = v(484, 648)
rs8 = v(466, 650)
rs9 = v(498, 688)
rs10 = v(484, 682)
rs11 = v(468, 684)

ra_0 = v(496, 714)
ra_1 = v(484, 708)
ra_2 = v(470, 710)

rft0 = v(500, 728)
rft1 = v(484, 724)
rft2 = v(468, 726)
rft3 = v(506, 744)
rft4 = v(486, 740)
rft5 = v(466, 742)
rft6 = v(512, 758)
rft7 = v(492, 756)
rft8 = v(470, 758)
rft9 = v(514, 770)
rft10 = v(504, 774)
rft11 = v(494, 776)
rft12 = v(484, 774)
rft13 = v(472, 770)

# ============================================================
# POLYGONS - Designed for organic flow and visual rhythm
# ============================================================

# ---- HEAD: dense, detailed topology ----
# Crown
poly([c0, c1, c4], 'Head')
poly([c0, c2, c4], 'Head')
poly([c1, c3, f0], 'Head')
poly([c1, c4, f1], 'Head')
poly([c1, f0, f1], 'Head')
poly([c4, f1, f2], 'Head')
poly([c4, c2, f3], 'Head')
poly([c4, f2, f3], 'Head')
poly([c2, c5, f4], 'Head')
poly([c2, f3, f4], 'Head')

# Forehead to brow
poly([f0, c3, t0], 'Head')
poly([f0, t0, t1], 'Head')
poly([f0, f1, t1], 'Head')
poly([f1, t1, t2], 'Head')
poly([f1, f2, t2], 'Head')
poly([f2, t2, t3], 'Head')
poly([f2, f3, t3], 'Head')
poly([f3, t3, t4], 'Head')
poly([f3, f4, t4], 'Head')
poly([f4, t4, t5], 'Head')
poly([f4, c5, t6], 'Head')
poly([f4, t5, t6], 'Head')

# Eye region
poly([t0, e0, t1], 'Head')
poly([t1, e0, e1], 'Head')
poly([t1, e1, t2], 'Head')
poly([t2, e1, e2], 'Head')
poly([t2, e2, t3], 'Head')
poly([t3, e3, e4], 'Head')
poly([t3, t4, e4], 'Head')
poly([t4, e4, e5], 'Head')
poly([t4, e5, t5], 'Head')
poly([t5, e5, e6], 'Head')
poly([t5, e6, t6], 'Head')
poly([e0, e1, e7], 'Head')
poly([e1, e2, e7], 'Head')
poly([e5, e6, e8], 'Head')
poly([e4, e5, e8], 'Head')
poly([t3, e2, e3], 'Head')

# Cheeks
poly([e0, e7, k0], 'Head')
poly([t0, e0, k0], 'Head')
poly([e6, e8, k1], 'Head')
poly([t6, e6, k1], 'Head')
poly([k0, e7, k2], 'Head')
poly([k1, e8, k3], 'Head')

# Nose
poly([e2, e3, n0], 'Head')
poly([e3, e4, n0], 'Head')
poly([e7, e2, n0], 'Head')
poly([e8, e4, n0], 'Head')
poly([n0, n1, n2], 'Head')
poly([n0, n3, n2], 'Head')
poly([e7, n0, n1], 'Head')
poly([e8, n0, n3], 'Head')

# Mouth
poly([n1, n2, m1], 'Head')
poly([n2, n3, m1], 'Head')
poly([n1, m0, m1], 'Head')
poly([n3, m2, m1], 'Head')
poly([k2, n1, m0], 'Head')
poly([k3, n3, m2], 'Head')
poly([m0, m1, m3], 'Head')
poly([m1, m2, m5], 'Head')
poly([m1, m3, m4], 'Head')
poly([m1, m4, m5], 'Head')

# Jaw
poly([k0, k2, j0], 'Head')
poly([k1, k3, j1], 'Head')
poly([k2, m0, j0], 'Head')
poly([k3, m2, j1], 'Head')
poly([j0, m0, j2], 'Head')
poly([j1, m2, j3], 'Head')
poly([m0, m3, j2], 'Head')
poly([m2, m5, j3], 'Head')
poly([j2, m3, j4], 'Head')
poly([j3, m5, j6], 'Head')
poly([m3, m4, j4], 'Head')
poly([m4, m5, j6], 'Head')
poly([j4, m4, j5], 'Head')
poly([j6, m4, j5], 'Head')

# ---- NECK ----
poly([j2, j4, nk0], 'Neck')
poly([j3, j6, nk2], 'Neck')
poly([j4, j5, nk0], 'Neck')
poly([j5, j6, nk2], 'Neck')
poly([j5, nk0, nk1], 'Neck')
poly([j5, nk1, nk2], 'Neck')
poly([nk0, nk1, nk3], 'Neck')
poly([nk1, nk2, nk5], 'Neck')
poly([nk1, nk3, nk4], 'Neck')
poly([nk1, nk4, nk5], 'Neck')
poly([nk3, nk4, nk6], 'Neck')
poly([nk4, nk5, nk8], 'Neck')
poly([nk4, nk6, nk7], 'Neck')
poly([nk4, nk7, nk8], 'Neck')

# ---- SHOULDERS ----
poly([nk6, s0, cb0], 'Shoulder')
poly([nk8, s1, cb2], 'Shoulder')
poly([nk6, nk7, cb0], 'Shoulder')
poly([nk7, nk8, cb2], 'Shoulder')
poly([nk7, cb0, cb1], 'Shoulder')
poly([nk7, cb1, cb2], 'Shoulder')
poly([s0, s2, cb0], 'Shoulder')
poly([s1, s3, cb2], 'Shoulder')
poly([s2, s4, s6], 'Shoulder')
poly([s3, s5, s7], 'Shoulder')
poly([s2, s4, ch0], 'Shoulder')
poly([s3, s5, ch4], 'Shoulder')
poly([s2, cb0, ch0], 'Shoulder')
poly([s3, cb2, ch4], 'Shoulder')

# ---- UPPER TORSO: larger polygons for "breathing" ----
poly([cb0, cb1, ch1], 'Upper Torso')
poly([cb1, cb2, ch3], 'Upper Torso')
poly([cb0, ch0, ch1], 'Upper Torso')
poly([cb2, ch4, ch3], 'Upper Torso')
poly([cb1, ch1, ch2], 'Upper Torso')
poly([cb1, ch2, ch3], 'Upper Torso')
poly([ch0, ch1, b0], 'Upper Torso')
poly([ch1, ch2, b1], 'Upper Torso')
poly([ch1, b0, b1], 'Upper Torso')
poly([ch2, ch3, b3], 'Upper Torso')
poly([ch2, b2, b3], 'Upper Torso')
poly([ch2, b1, b2], 'Upper Torso')
poly([ch3, ch4, b4], 'Upper Torso')
poly([ch3, b3, b4], 'Upper Torso')

# Bust to underbust
poly([b0, b1, ub0], 'Upper Torso')
poly([b1, ub0, ub1], 'Upper Torso')
poly([b1, b2, ub1], 'Upper Torso')
poly([b2, ub1, ub2], 'Upper Torso')
poly([b2, b3, ub3], 'Upper Torso')
poly([b2, ub2, ub3], 'Upper Torso')
poly([b3, b4, ub4], 'Upper Torso')
poly([b3, ub3, ub4], 'Upper Torso')

# Ribcage - open, elegant
poly([ub0, ub1, r0], 'Upper Torso')
poly([ub1, r0, r1], 'Upper Torso')
poly([ub1, ub2, r1], 'Upper Torso')
poly([ub2, r1, r2], 'Upper Torso')
poly([ub2, ub3, r3], 'Upper Torso')
poly([ub2, r2, r3], 'Upper Torso')
poly([ub3, ub4, r4], 'Upper Torso')
poly([ub3, r3, r4], 'Upper Torso')

# ---- WAIST: clean, open polygons ----
poly([r0, r1, w0], 'Lower Torso')
poly([r1, w0, w1], 'Lower Torso')
poly([r1, r2, w1], 'Lower Torso')
poly([r2, w1, w2], 'Lower Torso')
poly([r2, r3, w3], 'Lower Torso')
poly([r2, w2, w3], 'Lower Torso')
poly([r3, r4, w4], 'Lower Torso')
poly([r3, w3, w4], 'Lower Torso')

# Lower abdomen
poly([w0, w1, la0], 'Lower Torso')
poly([w1, la0, la1], 'Lower Torso')
poly([w1, w2, la1], 'Lower Torso')
poly([w2, la1, la2], 'Lower Torso')
poly([w2, w3, la3], 'Lower Torso')
poly([w2, la2, la3], 'Lower Torso')
poly([w3, w4, la4], 'Lower Torso')
poly([w3, la3, la4], 'Lower Torso')

# ---- HIPS: flowing lines ----
poly([la0, la1, h0], 'Hips')
poly([la1, h0, h1], 'Hips')
poly([la1, la2, h1], 'Hips')
poly([la2, h1, h2], 'Hips')
poly([la2, la3, h3], 'Hips')
poly([la2, h2, h3], 'Hips')
poly([la3, la4, h4], 'Hips')
poly([la3, h3, h4], 'Hips')

poly([h0, h1, lh0], 'Hips')
poly([h1, lh0, lh1], 'Hips')
poly([h1, h2, lh1], 'Hips')
poly([h2, lh1, lh2], 'Hips')
poly([h2, h3, lh3], 'Hips')
poly([h2, lh2, lh3], 'Hips')
poly([h3, h4, lh4], 'Hips')
poly([h3, lh3, lh4], 'Hips')

poly([lh0, lh1, g0], 'Hips')
poly([lh1, g0, g1], 'Hips')
poly([lh1, lh2, g1], 'Hips')
poly([lh2, g1, g2], 'Hips')
poly([lh2, lh3, g3], 'Hips')
poly([lh2, g2, g3], 'Hips')
poly([lh3, lh4, g4], 'Hips')
poly([lh3, g3, g4], 'Hips')

# Groin
poly([g0, g1, lth0], 'Hips')
poly([g1, g2, g5], 'Hips')
poly([g2, g3, g7], 'Hips')
poly([g3, g4, rth0], 'Hips')
poly([g2, g5, g6], 'Hips')
poly([g2, g6, g7], 'Hips')

# ---- LEFT UPPER ARM ----
poly([s6, lua0, lua1], 'Left Upper Arm')
poly([s6, ch0, lua1], 'Left Upper Arm')
poly([s4, s6, lua0], 'Left Upper Arm')
poly([lua0, lua1, lua2], 'Left Upper Arm')
poly([lua1, lua2, lua3], 'Left Upper Arm')
poly([lua2, lua3, lua4], 'Left Upper Arm')
poly([lua3, lua4, lua5], 'Left Upper Arm')
poly([lua4, lua5, lua6], 'Left Upper Arm')
poly([lua5, lua6, lua7], 'Left Upper Arm')
poly([lua6, lua7, le0], 'Left Upper Arm')
poly([lua7, le0, le1], 'Left Upper Arm')
poly([le0, le1, le2], 'Left Upper Arm')

# ---- LEFT FOREARM ----
poly([le0, le2, lfa0], 'Left Forearm')
poly([le1, le2, lfa1], 'Left Forearm')
poly([le2, lfa0, lfa1], 'Left Forearm')
poly([lfa0, lfa1, lfa2], 'Left Forearm')
poly([lfa1, lfa2, lfa3], 'Left Forearm')
poly([lfa2, lfa3, lfa4], 'Left Forearm')
poly([lfa3, lfa4, lfa5], 'Left Forearm')
poly([lfa4, lfa5, lfa6], 'Left Forearm')
poly([lfa5, lfa6, lfa7], 'Left Forearm')

# ---- LEFT HAND ----
poly([lfa6, lfa7, lh_0], 'Left Hand')
poly([lfa7, lh_0, lh_1], 'Left Hand')
poly([lh_0, lh_1, lh_2], 'Left Hand')
poly([lh_0, lh_2, lh_3], 'Left Hand')
poly([lh_1, lh_2, lh_4], 'Left Hand')
poly([lh_2, lh_3, lh_5], 'Left Hand')
poly([lh_2, lh_4, lh_5], 'Left Hand')
poly([lh_0, lh_3, lt0], 'Left Hand')
poly([lt0, lt1, lh_3], 'Left Hand')
poly([lt1, lt2, lh_3], 'Left Hand')
poly([lh_3, lh_5, lf0], 'Left Hand')
poly([lf0, lf1, lh_5], 'Left Hand')
poly([lh_5, lf2, lf3], 'Left Hand')
poly([lh_5, lf2, lf4], 'Left Hand')
poly([lf4, lf5, lh_5], 'Left Hand')
poly([lh_4, lh_5, lf6], 'Left Hand')
poly([lf6, lf7, lh_4], 'Left Hand')

# ---- RIGHT UPPER ARM ----
poly([s7, rua0, rua1], 'Right Upper Arm')
poly([s7, ch4, rua1], 'Right Upper Arm')
poly([s5, s7, rua0], 'Right Upper Arm')
poly([rua0, rua1, rua2], 'Right Upper Arm')
poly([rua1, rua2, rua3], 'Right Upper Arm')
poly([rua2, rua3, rua4], 'Right Upper Arm')
poly([rua3, rua4, rua5], 'Right Upper Arm')
poly([rua4, rua5, rua6], 'Right Upper Arm')
poly([rua5, rua6, rua7], 'Right Upper Arm')
poly([rua6, rua7, re0], 'Right Upper Arm')
poly([rua7, re0, re1], 'Right Upper Arm')
poly([re0, re1, re2], 'Right Upper Arm')

# ---- RIGHT FOREARM ----
poly([re0, re2, rfa0], 'Right Forearm')
poly([re1, re2, rfa1], 'Right Forearm')
poly([re2, rfa0, rfa1], 'Right Forearm')
poly([rfa0, rfa1, rfa2], 'Right Forearm')
poly([rfa1, rfa2, rfa3], 'Right Forearm')
poly([rfa2, rfa3, rfa4], 'Right Forearm')
poly([rfa3, rfa4, rfa5], 'Right Forearm')
poly([rfa4, rfa5, rfa6], 'Right Forearm')
poly([rfa5, rfa6, rfa7], 'Right Forearm')

# ---- RIGHT HAND ----
poly([rfa6, rfa7, rh_0], 'Right Hand')
poly([rfa7, rh_0, rh_1], 'Right Hand')
poly([rh_0, rh_1, rh_2], 'Right Hand')
poly([rh_0, rh_2, rh_3], 'Right Hand')
poly([rh_1, rh_2, rh_4], 'Right Hand')
poly([rh_2, rh_3, rh_5], 'Right Hand')
poly([rh_2, rh_4, rh_5], 'Right Hand')
poly([rh_0, rh_3, rt0], 'Right Hand')
poly([rt0, rt1, rh_3], 'Right Hand')
poly([rt1, rt2, rh_3], 'Right Hand')
poly([rh_3, rh_5, rf0], 'Right Hand')
poly([rf0, rf1, rh_5], 'Right Hand')
poly([rh_5, rf2, rf3], 'Right Hand')
poly([rh_5, rf2, rf4], 'Right Hand')
poly([rf4, rf5, rh_5], 'Right Hand')
poly([rh_4, rh_5, rf6], 'Right Hand')
poly([rf6, rf7, rh_4], 'Right Hand')

# ---- LEFT THIGH ----
poly([g0, lth0, lth1], 'Left Thigh')
poly([g1, g5, lth1], 'Left Thigh')
poly([g0, g1, lth1], 'Left Thigh')
poly([lth0, lth1, lth2], 'Left Thigh')
poly([lth1, lth2, lth3], 'Left Thigh')
poly([lth1, lth3, lth4], 'Left Thigh')
poly([g5, lth1, lth4], 'Left Thigh')
poly([lth2, lth3, lth5], 'Left Thigh')
poly([lth3, lth5, lth6], 'Left Thigh')
poly([lth3, lth4, lth7], 'Left Thigh')
poly([lth3, lth6, lth7], 'Left Thigh')
poly([lth5, lth6, lth8], 'Left Thigh')
poly([lth6, lth8, lth9], 'Left Thigh')
poly([lth6, lth7, lth10], 'Left Thigh')
poly([lth6, lth9, lth10], 'Left Thigh')

# Knee
poly([lth8, lth9, lk0], 'Left Thigh')
poly([lth9, lk0, lk1], 'Left Thigh')
poly([lth9, lth10, lk2], 'Left Thigh')
poly([lth9, lk1, lk2], 'Left Thigh')
poly([lk0, lk1, lk4], 'Left Thigh')
poly([lk1, lk4, lk3], 'Left Thigh')
poly([lk1, lk2, lk5], 'Left Thigh')
poly([lk1, lk3, lk5], 'Left Thigh')

# ---- LEFT SHIN ----
poly([lk4, lk3, ls0], 'Left Calf')
poly([lk3, ls0, ls1], 'Left Calf')
poly([lk3, lk5, ls2], 'Left Calf')
poly([lk3, ls1, ls2], 'Left Calf')
poly([ls0, ls1, ls3], 'Left Calf')
poly([ls1, ls3, ls4], 'Left Calf')
poly([ls1, ls2, ls5], 'Left Calf')
poly([ls1, ls4, ls5], 'Left Calf')
poly([ls3, ls4, ls6], 'Left Calf')
poly([ls4, ls6, ls7], 'Left Calf')
poly([ls4, ls5, ls8], 'Left Calf')
poly([ls4, ls7, ls8], 'Left Calf')
poly([ls6, ls7, ls9], 'Left Calf')
poly([ls7, ls9, ls10], 'Left Calf')
poly([ls7, ls8, ls11], 'Left Calf')
poly([ls7, ls10, ls11], 'Left Calf')

# Ankle
poly([ls9, ls10, la_0], 'Left Calf')
poly([ls10, la_0, la_1], 'Left Calf')
poly([ls10, ls11, la_2], 'Left Calf')
poly([ls10, la_1, la_2], 'Left Calf')

# ---- LEFT FOOT ----
poly([la_0, la_1, ft0], 'Left Foot')
poly([la_1, ft0, ft1], 'Left Foot')
poly([la_1, la_2, ft2], 'Left Foot')
poly([la_1, ft1, ft2], 'Left Foot')
poly([ft0, ft1, ft3], 'Left Foot')
poly([ft1, ft3, ft4], 'Left Foot')
poly([ft1, ft2, ft5], 'Left Foot')
poly([ft1, ft4, ft5], 'Left Foot')
poly([ft3, ft4, ft6], 'Left Foot')
poly([ft4, ft6, ft7], 'Left Foot')
poly([ft4, ft5, ft8], 'Left Foot')
poly([ft4, ft7, ft8], 'Left Foot')
poly([ft6, ft7, ft9], 'Left Foot')
poly([ft7, ft9, ft10], 'Left Foot')
poly([ft7, ft10, ft11], 'Left Foot')
poly([ft7, ft11, ft12], 'Left Foot')
poly([ft7, ft8, ft12], 'Left Foot')
poly([ft8, ft12, ft13], 'Left Foot')

# ---- RIGHT THIGH ----
poly([g4, rth0, rth1], 'Right Thigh')
poly([g3, g7, rth1], 'Right Thigh')
poly([g3, g4, rth1], 'Right Thigh')
poly([rth0, rth1, rth2], 'Right Thigh')
poly([rth1, rth2, rth3], 'Right Thigh')
poly([rth1, rth3, rth4], 'Right Thigh')
poly([g7, rth1, rth4], 'Right Thigh')
poly([rth2, rth3, rth5], 'Right Thigh')
poly([rth3, rth5, rth6], 'Right Thigh')
poly([rth3, rth4, rth7], 'Right Thigh')
poly([rth3, rth6, rth7], 'Right Thigh')
poly([rth5, rth6, rth8], 'Right Thigh')
poly([rth6, rth8, rth9], 'Right Thigh')
poly([rth6, rth7, rth10], 'Right Thigh')
poly([rth6, rth9, rth10], 'Right Thigh')

# Knee
poly([rth8, rth9, rk0], 'Right Thigh')
poly([rth9, rk0, rk1], 'Right Thigh')
poly([rth9, rth10, rk2], 'Right Thigh')
poly([rth9, rk1, rk2], 'Right Thigh')
poly([rk0, rk1, rk4], 'Right Thigh')
poly([rk1, rk4, rk3], 'Right Thigh')
poly([rk1, rk2, rk5], 'Right Thigh')
poly([rk1, rk3, rk5], 'Right Thigh')

# ---- RIGHT SHIN ----
poly([rk4, rk3, rs0], 'Right Calf')
poly([rk3, rs0, rs1], 'Right Calf')
poly([rk3, rk5, rs2], 'Right Calf')
poly([rk3, rs1, rs2], 'Right Calf')
poly([rs0, rs1, rs3], 'Right Calf')
poly([rs1, rs3, rs4], 'Right Calf')
poly([rs1, rs2, rs5], 'Right Calf')
poly([rs1, rs4, rs5], 'Right Calf')
poly([rs3, rs4, rs6], 'Right Calf')
poly([rs4, rs6, rs7], 'Right Calf')
poly([rs4, rs5, rs8], 'Right Calf')
poly([rs4, rs7, rs8], 'Right Calf')
poly([rs6, rs7, rs9], 'Right Calf')
poly([rs7, rs9, rs10], 'Right Calf')
poly([rs7, rs8, rs11], 'Right Calf')
poly([rs7, rs10, rs11], 'Right Calf')

# Ankle
poly([rs9, rs10, ra_0], 'Right Calf')
poly([rs10, ra_0, ra_1], 'Right Calf')
poly([rs10, rs11, ra_2], 'Right Calf')
poly([rs10, ra_1, ra_2], 'Right Calf')

# ---- RIGHT FOOT ----
poly([ra_0, ra_1, rft0], 'Right Foot')
poly([ra_1, rft0, rft1], 'Right Foot')
poly([ra_1, ra_2, rft2], 'Right Foot')
poly([ra_1, rft1, rft2], 'Right Foot')
poly([rft0, rft1, rft3], 'Right Foot')
poly([rft1, rft3, rft4], 'Right Foot')
poly([rft1, rft2, rft5], 'Right Foot')
poly([rft1, rft4, rft5], 'Right Foot')
poly([rft3, rft4, rft6], 'Right Foot')
poly([rft4, rft6, rft7], 'Right Foot')
poly([rft4, rft5, rft8], 'Right Foot')
poly([rft4, rft7, rft8], 'Right Foot')
poly([rft6, rft7, rft9], 'Right Foot')
poly([rft7, rft9, rft10], 'Right Foot')
poly([rft7, rft10, rft11], 'Right Foot')
poly([rft7, rft11, rft12], 'Right Foot')
poly([rft7, rft8, rft12], 'Right Foot')
poly([rft8, rft12, rft13], 'Right Foot')

# Torso-arm connections
poly([ch0, b0, lua1], 'Upper Torso')
poly([ch4, b4, rua1], 'Upper Torso')

# ============================================================
# RENDER
# ============================================================
region_order = ['Head', 'Neck', 'Shoulder', 'Upper Torso', 'Lower Torso', 'Hips',
                'Left Upper Arm', 'Right Upper Arm', 'Left Forearm', 'Right Forearm',
                'Left Hand', 'Right Hand',
                'Left Thigh', 'Right Thigh', 'Left Calf', 'Right Calf',
                'Left Foot', 'Right Foot']

grouped = {}
for indices, region in polygons:
    grouped.setdefault(region, []).append(indices)

svg_lines = []
svg_lines.append('<?xml version="1.0" encoding="UTF-8"?>')
svg_lines.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" fill="none">')
svg_lines.append('  <style>')
svg_lines.append('    .facet { fill: none; stroke: #4d4d4d; stroke-width: 0.7; stroke-linejoin: round; }')
svg_lines.append('  </style>')

# Center line
svg_lines.append('  <line x1="400" y1="22" x2="400" y2="418" stroke="#d0d0d0" stroke-width="0.25" stroke-dasharray="4,6"/>')

for region in region_order:
    if region not in grouped:
        continue
    rid = region.lower().replace(' ', '-')
    svg_lines.append(f'  <g id="{rid}">')
    for indices in grouped[region]:
        pts = ' '.join(f'{vertices[i][0]},{vertices[i][1]}' for i in indices)
        svg_lines.append(f'    <polygon class="facet" data-region="{region}" points="{pts}"/>')
    svg_lines.append('  </g>')

svg_lines.append('</svg>')
svg_content = '\n'.join(svg_lines)

with open('/var/lib/freelancer/projects/40461616/female-front-wireframe.svg', 'w') as f:
    f.write(svg_content)

# HTML
html_svg = svg_content.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Low-Poly Female Front — Wireframe Topology</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300&family=Outfit:wght@200;300&display=swap');
  *{margin:0;padding:0;box-sizing:border-box}
  body{
    background:#fff;
    min-height:100vh;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    font-family:'Outfit',sans-serif;
    color:#444;
  }
  .page-wrapper{
    display:flex;
    flex-direction:column;
    align-items:center;
    padding:30px 20px 50px;
    max-width:600px;
  }
  .title-block{
    text-align:center;
    margin-bottom:16px;
  }
  .title-block h1{
    font-family:'Cormorant Garamond',serif;
    font-weight:300;
    font-size:1.5rem;
    letter-spacing:0.12em;
    text-transform:uppercase;
    color:#666;
  }
  .title-block .sub{
    font-weight:200;
    font-size:0.6rem;
    letter-spacing:0.25em;
    text-transform:uppercase;
    color:#bbb;
    margin-top:3px;
  }
  .svg-container{
    width:100%;
    max-width:520px;
  }
  .svg-container svg{width:100%;height:auto;display:block}
  .facet{
    fill:none;
    stroke:#4d4d4d;
    stroke-width:0.7;
    stroke-linejoin:round;
    transition:fill 0.15s ease, stroke 0.15s ease;
    cursor:pointer;
  }
  .facet:hover{
    fill:rgba(80,80,80,0.04);
    stroke:#333;
    stroke-width:0.9;
  }
  .facet.active{
    fill:rgba(60,60,60,0.07);
    stroke:#222;
    stroke-width:1.1;
  }
  .tip{
    position:fixed;pointer-events:none;
    background:rgba(255,255,255,0.97);
    border:1px solid #e0e0e0;
    color:#777;font-weight:300;
    font-size:0.55rem;letter-spacing:0.1em;
    text-transform:uppercase;
    padding:3px 10px;border-radius:1px;
    opacity:0;transition:opacity 0.12s;z-index:99;
    white-space:nowrap;
  }
  .tip.on{opacity:1}
  .foot{color:#ccc;font-size:0.45rem;letter-spacing:0.2em;text-transform:uppercase;margin-top:12px;font-weight:200}
</style>
</head>
<body>
<div class="page-wrapper">
  <div class="title-block">
    <h1>Female Front &mdash; Wireframe Topology</h1>
    <div class="sub">Premium Low-Poly &bull; Beauty-Tech Series</div>
  </div>
  <div class="svg-container">
''' + html_svg + '''
  </div>
  <span class="foot">Hover to explore &bull; Click to select</span>
</div>
<div class="tip" id="tip"></div>
<script>
(function(){
  const t=document.getElementById('tip');let a=null;
  document.querySelectorAll('.facet').forEach(f=>{
    f.addEventListener('mouseenter',()=>{t.textContent=f.dataset.region;t.classList.add('on')});
    f.addEventListener('mousemove',e=>{t.style.left=(e.clientX+12)+'px';t.style.top=(e.clientY-8)+'px'});
    f.addEventListener('mouseleave',()=>t.classList.remove('on'));
    f.addEventListener('click',e=>{e.stopPropagation();if(a)a.classList.remove('active');if(a===f){a=null;return}f.classList.add('active');a=f});
  });
  document.addEventListener('click',()=>{if(a){a.classList.remove('active');a=null}});
})();
</script>
</body>
</html>'''

with open('/var/lib/freelancer/projects/40461616/demo-wireframe.html', 'w') as f:
    f.write(html)

print(f"Total polygons: {len(polygons)}")
print(f"Total vertices: {len(vertices)}")
for r in region_order:
    if r in grouped:
        print(f"  {r}: {len(grouped[r])}")
