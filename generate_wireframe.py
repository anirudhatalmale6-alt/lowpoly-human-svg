#!/usr/bin/env python3
"""
Generate premium wireframe topology SVG - female front view.
Clean grey linework, transparent background, A-pose, retopology style.
Matching client reference images: organic polygon flow following muscle groups.
"""

vertices = []
polygons = []

def v(x, y):
    vertices.append((round(x, 1), round(y, 1)))
    return len(vertices) - 1

def poly(indices, region):
    polygons.append((indices, region))

# ============================================================
# FEMALE FRONT VIEW - A-POSE
# ViewBox: 0 0 700 1100
# Center: x=350, Crown: y=20, Feet: y=1080
# Proportions: ~7.5 head heights (female)
# ============================================================

# HEAD HEIGHT ~130px (head = y 20 to ~150)
# Total figure ~1060px

# ---- CROWN / TOP OF HEAD ----
v0 = v(350, 20)    # 0 crown top center
v1 = v(330, 28)    # 1 crown left
v2 = v(370, 28)    # 2 crown right
v3 = v(312, 40)    # 3 upper left
v4 = v(350, 36)    # 4 crown mid
v5 = v(388, 40)    # 5 upper right

# ---- FOREHEAD ----
v6 = v(305, 56)    # 6 forehead left
v7 = v(350, 50)    # 7 forehead center
v8 = v(395, 56)    # 8 forehead right
v9 = v(302, 72)    # 9 temple left
v10 = v(398, 72)   # 10 temple right

# ---- BROW / EYE LINE ----
v11 = v(306, 82)   # 11 brow outer left
v12 = v(322, 80)   # 12 brow inner left
v13 = v(350, 78)   # 13 brow center
v14 = v(378, 80)   # 14 brow inner right
v15 = v(394, 82)   # 15 brow outer right

# ---- EYES ----
v16 = v(304, 90)   # 16 eye outer left
v17 = v(318, 88)   # 17 eye top left
v18 = v(330, 90)   # 18 eye inner left
v19 = v(350, 88)   # 19 nose bridge
v20 = v(370, 90)   # 20 eye inner right
v21 = v(382, 88)   # 21 eye top right
v22 = v(396, 90)   # 22 eye outer right
v23 = v(316, 96)   # 23 eye bottom left
v24 = v(384, 96)   # 24 eye bottom right

# ---- NOSE ----
v25 = v(350, 98)   # 25 nose mid
v26 = v(342, 110)  # 26 nostril left
v27 = v(350, 112)  # 27 nose tip
v28 = v(358, 110)  # 28 nostril right

# ---- CHEEKS ----
v29 = v(300, 104)  # 29 cheek outer left
v30 = v(400, 104)  # 30 cheek outer right
v31 = v(302, 118)  # 31 lower cheek left
v32 = v(398, 118)  # 32 lower cheek right

# ---- MOUTH ----
v33 = v(334, 122)  # 33 mouth left
v34 = v(350, 120)  # 34 above mouth
v35 = v(366, 122)  # 35 mouth right
v36 = v(350, 128)  # 36 below mouth

# ---- JAW / CHIN ----
v37 = v(308, 132)  # 37 jaw left
v38 = v(392, 132)  # 38 jaw right
v39 = v(318, 142)  # 39 jaw angle left
v40 = v(382, 142)  # 40 jaw angle right
v41 = v(332, 148)  # 41 chin left
v42 = v(350, 152)  # 42 chin
v43 = v(368, 148)  # 43 chin right

# ---- NECK ----
v44 = v(326, 160)  # 44 neck left
v45 = v(350, 158)  # 45 neck center
v46 = v(374, 160)  # 46 neck right
v47 = v(322, 174)  # 47 neck base left
v48 = v(350, 172)  # 48 neck base center
v49 = v(378, 174)  # 49 neck base right

# ---- SHOULDERS ----
v50 = v(290, 180)  # 50 inner shoulder left
v51 = v(410, 180)  # 51 inner shoulder right
v52 = v(254, 186)  # 52 shoulder top left
v53 = v(446, 186)  # 53 shoulder top right
v54 = v(222, 196)  # 54 deltoid top left
v55 = v(478, 196)  # 55 deltoid top right
v56 = v(206, 212)  # 56 deltoid mid left
v57 = v(494, 212)  # 57 deltoid mid right

# ---- COLLARBONE ----
v58 = v(304, 186)  # 58 clavicle left
v59 = v(350, 182)  # 59 clavicle center
v60 = v(396, 186)  # 60 clavicle right

# ---- UPPER CHEST ----
v61 = v(296, 204)  # 61 chest outer left
v62 = v(350, 198)  # 62 chest center top
v63 = v(404, 204)  # 63 chest outer right
v64 = v(290, 222)  # 64 chest mid left
v65 = v(350, 216)  # 65 chest center mid
v66 = v(410, 222)  # 66 chest mid right
v67 = v(286, 240)  # 67 under-chest left
v68 = v(350, 234)  # 68 sternum
v69 = v(414, 240)  # 69 under-chest right

# ---- RIBCAGE ----
v70 = v(284, 260)  # 70 rib outer left
v71 = v(316, 256)  # 71 rib inner left
v72 = v(350, 254)  # 72 rib center
v73 = v(384, 256)  # 73 rib inner right
v74 = v(416, 260)  # 74 rib outer right

# ---- WAIST (narrowest) ----
v75 = v(288, 282)  # 75 waist outer left
v76 = v(320, 278)  # 76 waist inner left
v77 = v(350, 276)  # 77 waist center (navel)
v78 = v(380, 278)  # 78 waist inner right
v79 = v(412, 282)  # 79 waist outer right

# ---- LOWER ABDOMEN ----
v80 = v(286, 304)  # 80 abdomen outer left
v81 = v(318, 300)  # 81 abdomen inner left
v82 = v(350, 298)  # 82 abdomen center
v83 = v(382, 300)  # 83 abdomen inner right
v84 = v(414, 304)  # 84 abdomen outer right

# ---- HIPS ----
v85 = v(278, 326)  # 85 hip left
v86 = v(312, 322)  # 86 hip inner left
v87 = v(350, 320)  # 87 hip center
v88 = v(388, 322)  # 88 hip inner right
v89 = v(422, 326)  # 89 hip right

v90 = v(274, 348)  # 90 lower hip left
v91 = v(308, 342)  # 91 lower hip inner left
v92 = v(350, 338)  # 92 lower hip center
v93 = v(392, 342)  # 93 lower hip inner right
v94 = v(426, 348)  # 94 lower hip right

# ---- GROIN / LEG SPLIT ----
v95 = v(278, 368)  # 95 groin outer left
v96 = v(312, 362)  # 96 groin inner left
v97 = v(350, 358)  # 97 groin center
v98 = v(388, 362)  # 98 groin inner right
v99 = v(422, 368)  # 99 groin outer right
v100 = v(320, 382) # 100 inner thigh top left
v101 = v(350, 386) # 101 crotch bottom
v102 = v(380, 382) # 102 inner thigh top right

# ---- LEFT UPPER ARM ----
# Angled ~35° out from shoulder
v103 = v(196, 226) # 103 outer bicep 1
v104 = v(218, 222) # 104 inner bicep 1
v105 = v(182, 248) # 105 outer bicep 2
v106 = v(204, 244) # 106 inner bicep 2
v107 = v(170, 270) # 107 outer bicep 3
v108 = v(192, 266) # 108 inner bicep 3
v109 = v(160, 292) # 109 outer bicep 4
v110 = v(180, 288) # 110 inner bicep 4

# ---- LEFT ELBOW ----
v111 = v(152, 308) # 111 elbow outer
v112 = v(170, 304) # 112 elbow inner
v113 = v(160, 312) # 113 elbow point

# ---- LEFT FOREARM ----
v114 = v(146, 328) # 114 outer forearm 1
v115 = v(164, 324) # 115 inner forearm 1
v116 = v(140, 350) # 116 outer forearm 2
v117 = v(158, 346) # 117 inner forearm 2
v118 = v(134, 372) # 118 outer forearm 3
v119 = v(152, 368) # 119 inner forearm 3
v120 = v(128, 392) # 120 wrist outer
v121 = v(146, 388) # 121 wrist inner

# ---- LEFT HAND ----
v122 = v(124, 404) # 122 palm outer
v123 = v(140, 400) # 123 palm inner
v124 = v(132, 408) # 124 palm center
v125 = v(120, 416) # 125 palm base outer
v126 = v(142, 414) # 126 palm base inner
v127 = v(130, 420) # 127 palm bottom

# Left fingers
v128 = v(116, 410) # 128 thumb base
v129 = v(110, 420) # 129 thumb tip
v130 = v(116, 430) # 130 index tip
v131 = v(118, 424) # 131 index mid
v132 = v(126, 434) # 132 middle tip
v133 = v(126, 426) # 133 middle mid
v134 = v(134, 432) # 134 ring tip
v135 = v(134, 424) # 135 ring mid
v136 = v(142, 426) # 136 pinky tip
v137 = v(140, 420) # 137 pinky mid

# ---- RIGHT UPPER ARM (mirror) ----
v138 = v(504, 226) # 138
v139 = v(482, 222) # 139
v140 = v(518, 248) # 140
v141 = v(496, 244) # 141
v142 = v(530, 270) # 142
v143 = v(508, 266) # 143
v144 = v(540, 292) # 144
v145 = v(520, 288) # 145

# ---- RIGHT ELBOW ----
v146 = v(548, 308) # 146
v147 = v(530, 304) # 147
v148 = v(540, 312) # 148

# ---- RIGHT FOREARM ----
v149 = v(554, 328) # 149
v150 = v(536, 324) # 150
v151 = v(560, 350) # 151
v152 = v(542, 346) # 152
v153 = v(566, 372) # 153
v154 = v(548, 368) # 154
v155 = v(572, 392) # 155
v156 = v(554, 388) # 156

# ---- RIGHT HAND ----
v157 = v(576, 404) # 157
v158 = v(560, 400) # 158
v159 = v(568, 408) # 159
v160 = v(580, 416) # 160
v161 = v(558, 414) # 161
v162 = v(570, 420) # 162
v163 = v(584, 410) # 163
v164 = v(590, 420) # 164
v165 = v(584, 430) # 165
v166 = v(582, 424) # 166
v167 = v(574, 434) # 167
v168 = v(574, 426) # 168
v169 = v(566, 432) # 169
v170 = v(566, 424) # 170
v171 = v(558, 426) # 171
v172 = v(560, 420) # 172

# ---- LEFT THIGH ----
v173 = v(272, 388) # 173 outer thigh top
v174 = v(268, 410) # 174 outer thigh 2
v175 = v(296, 404) # 175 front thigh
v176 = v(264, 436) # 176 outer thigh 3
v177 = v(290, 430) # 177 front thigh 2
v178 = v(316, 424) # 178 inner thigh 2
v179 = v(260, 462) # 179 outer thigh 4
v180 = v(286, 458) # 180 front thigh 3
v181 = v(312, 452) # 181 inner thigh 3
v182 = v(258, 488) # 182 outer knee approach
v183 = v(282, 484) # 183 front knee approach
v184 = v(308, 480) # 184 inner knee approach

# ---- LEFT KNEE ----
v185 = v(256, 504) # 185 knee outer
v186 = v(280, 502) # 186 kneecap
v187 = v(306, 500) # 187 knee inner
v188 = v(268, 516) # 188 below knee

# ---- LEFT SHIN ----
v189 = v(258, 532) # 189 shin outer 1
v190 = v(280, 528) # 190 shin front 1
v191 = v(302, 530) # 191 shin inner 1
v192 = v(260, 562) # 192 shin outer 2
v193 = v(278, 558) # 193 shin front 2
v194 = v(298, 560) # 194 shin inner 2
v195 = v(262, 592) # 195 shin outer 3
v196 = v(278, 588) # 196 shin front 3
v197 = v(296, 590) # 197 shin inner 3
v198 = v(264, 618) # 198 shin outer 4
v199 = v(278, 614) # 199 shin front 4
v200 = v(294, 616) # 200 shin inner 4

# ---- LEFT ANKLE ----
v201 = v(264, 636) # 201 ankle outer
v202 = v(278, 632) # 202 ankle center
v203 = v(292, 634) # 203 ankle inner

# ---- LEFT FOOT ----
v204 = v(258, 648) # 204 heel outer
v205 = v(278, 646) # 205 heel center
v206 = v(294, 648) # 206 heel inner
v207 = v(252, 662) # 207 mid foot outer
v208 = v(276, 660) # 208 mid foot center
v209 = v(296, 662) # 209 mid foot inner
v210 = v(248, 676) # 210 ball outer
v211 = v(268, 674) # 211 ball center
v212 = v(290, 676) # 212 ball inner
# Toes
v213 = v(246, 688) # 213 toe 1
v214 = v(256, 692) # 214 toe 2
v215 = v(266, 694) # 215 toe 3
v216 = v(276, 692) # 216 toe 4
v217 = v(288, 688) # 217 toe 5

# ---- RIGHT THIGH (mirror) ----
v218 = v(428, 388) # 218
v219 = v(432, 410) # 219
v220 = v(404, 404) # 220
v221 = v(436, 436) # 221
v222 = v(410, 430) # 222
v223 = v(384, 424) # 223
v224 = v(440, 462) # 224
v225 = v(414, 458) # 225
v226 = v(388, 452) # 226
v227 = v(442, 488) # 227
v228 = v(418, 484) # 228
v229 = v(392, 480) # 229

# ---- RIGHT KNEE ----
v230 = v(444, 504) # 230
v231 = v(420, 502) # 231
v232 = v(394, 500) # 232
v233 = v(432, 516) # 233

# ---- RIGHT SHIN ----
v234 = v(442, 532) # 234
v235 = v(420, 528) # 235
v236 = v(398, 530) # 236
v237 = v(440, 562) # 237
v238 = v(422, 558) # 238
v239 = v(402, 560) # 239
v240 = v(438, 592) # 240
v241 = v(422, 588) # 241
v242 = v(404, 590) # 242
v243 = v(436, 618) # 243
v244 = v(422, 614) # 244
v245 = v(406, 616) # 245

# ---- RIGHT ANKLE ----
v246 = v(436, 636) # 246
v247 = v(422, 632) # 247
v248 = v(408, 634) # 248

# ---- RIGHT FOOT ----
v249 = v(442, 648) # 249
v250 = v(422, 646) # 250
v251 = v(406, 648) # 251
v252 = v(448, 662) # 252
v253 = v(424, 660) # 253
v254 = v(404, 662) # 254
v255 = v(452, 676) # 255
v256 = v(432, 674) # 256
v257 = v(410, 676) # 257
v258 = v(454, 688) # 258
v259 = v(444, 692) # 259
v260 = v(434, 694) # 260
v261 = v(424, 692) # 261
v262 = v(412, 688) # 262

# ============================================================
# HEAD POLYGONS
# ============================================================

# Crown
poly([0, 1, 4], 'Head')
poly([0, 2, 4], 'Head')
poly([1, 3, 4], 'Head')
poly([2, 5, 4], 'Head')

# Forehead
poly([3, 6, 7], 'Head')
poly([3, 4, 7], 'Head')
poly([4, 5, 7], 'Head')
poly([5, 8, 7], 'Head')
poly([6, 9, 11], 'Head')
poly([6, 7, 12], 'Head')
poly([6, 11, 12], 'Head')
poly([7, 8, 14], 'Head')
poly([7, 12, 13], 'Head')
poly([7, 13, 14], 'Head')
poly([8, 10, 15], 'Head')
poly([8, 14, 15], 'Head')

# Eyes
poly([11, 16, 17], 'Head')
poly([11, 12, 17], 'Head')
poly([12, 17, 18], 'Head')
poly([12, 13, 18], 'Head')
poly([13, 19, 18], 'Head')
poly([13, 19, 20], 'Head')
poly([13, 14, 20], 'Head')
poly([14, 20, 21], 'Head')
poly([14, 15, 21], 'Head')
poly([15, 21, 22], 'Head')
poly([16, 17, 23], 'Head')
poly([17, 18, 23], 'Head')
poly([21, 22, 24], 'Head')
poly([20, 21, 24], 'Head')

# Cheeks + nose
poly([16, 23, 29], 'Head')
poly([9, 16, 29], 'Head')
poly([22, 24, 30], 'Head')
poly([10, 22, 30], 'Head')
poly([18, 19, 25], 'Head')
poly([19, 20, 25], 'Head')
poly([23, 18, 25], 'Head')
poly([24, 20, 25], 'Head')
poly([25, 26, 27], 'Head')
poly([25, 28, 27], 'Head')
poly([23, 25, 26], 'Head')
poly([24, 25, 28], 'Head')
poly([29, 23, 31], 'Head')
poly([30, 24, 32], 'Head')

# Mouth
poly([26, 33, 34], 'Head')
poly([26, 27, 34], 'Head')
poly([27, 28, 34], 'Head')
poly([28, 35, 34], 'Head')
poly([33, 34, 36], 'Head')
poly([34, 35, 36], 'Head')
poly([23, 26, 31], 'Head')
poly([24, 28, 32], 'Head')
poly([31, 26, 33], 'Head')
poly([32, 28, 35], 'Head')

# Jaw
poly([31, 33, 37], 'Head')
poly([32, 35, 38], 'Head')
poly([29, 31, 37], 'Head')
poly([30, 32, 38], 'Head')
poly([37, 33, 39], 'Head')
poly([38, 35, 40], 'Head')
poly([33, 36, 39], 'Head')
poly([35, 36, 40], 'Head')
poly([39, 36, 41], 'Head')
poly([40, 36, 43], 'Head')
poly([36, 41, 42], 'Head')
poly([36, 43, 42], 'Head')

# ============================================================
# NECK
# ============================================================
poly([39, 41, 44], 'Neck')
poly([40, 43, 46], 'Neck')
poly([41, 42, 44], 'Neck')
poly([42, 43, 46], 'Neck')
poly([42, 44, 45], 'Neck')
poly([42, 46, 45], 'Neck')
poly([44, 45, 47], 'Neck')
poly([45, 46, 49], 'Neck')
poly([45, 47, 48], 'Neck')
poly([45, 49, 48], 'Neck')

# ============================================================
# SHOULDERS
# ============================================================
poly([47, 50, 58], 'Shoulder')
poly([49, 51, 60], 'Shoulder')
poly([47, 48, 58], 'Shoulder')
poly([48, 49, 60], 'Shoulder')
poly([48, 58, 59], 'Shoulder')
poly([48, 59, 60], 'Shoulder')
poly([50, 52, 58], 'Shoulder')
poly([51, 53, 60], 'Shoulder')
poly([52, 54, 56], 'Shoulder')
poly([53, 55, 57], 'Shoulder')
poly([52, 56, 61], 'Shoulder')
poly([53, 57, 63], 'Shoulder')
poly([52, 58, 61], 'Shoulder')
poly([53, 60, 63], 'Shoulder')

# ============================================================
# UPPER TORSO
# ============================================================
poly([58, 59, 62], 'Upper Torso')
poly([59, 60, 62], 'Upper Torso')
poly([58, 61, 62], 'Upper Torso')
poly([60, 63, 62], 'Upper Torso')
poly([61, 62, 64], 'Upper Torso')
poly([62, 63, 66], 'Upper Torso')
poly([62, 64, 65], 'Upper Torso')
poly([62, 65, 66], 'Upper Torso')
poly([64, 65, 67], 'Upper Torso')
poly([65, 66, 69], 'Upper Torso')
poly([65, 67, 68], 'Upper Torso')
poly([65, 68, 69], 'Upper Torso')
poly([67, 68, 71], 'Upper Torso')
poly([68, 69, 73], 'Upper Torso')
poly([67, 70, 71], 'Upper Torso')
poly([69, 74, 73], 'Upper Torso')
poly([68, 71, 72], 'Upper Torso')
poly([68, 72, 73], 'Upper Torso')

# ============================================================
# WAIST / LOWER TORSO
# ============================================================
poly([70, 71, 75], 'Lower Torso')
poly([71, 75, 76], 'Lower Torso')
poly([71, 72, 76], 'Lower Torso')
poly([72, 76, 77], 'Lower Torso')
poly([72, 73, 78], 'Lower Torso')
poly([72, 77, 78], 'Lower Torso')
poly([73, 74, 79], 'Lower Torso')
poly([73, 78, 79], 'Lower Torso')

poly([75, 76, 80], 'Lower Torso')
poly([76, 80, 81], 'Lower Torso')
poly([76, 77, 81], 'Lower Torso')
poly([77, 81, 82], 'Lower Torso')
poly([77, 78, 83], 'Lower Torso')
poly([77, 82, 83], 'Lower Torso')
poly([78, 79, 84], 'Lower Torso')
poly([78, 83, 84], 'Lower Torso')

# ============================================================
# HIPS
# ============================================================
poly([80, 81, 85], 'Hips')
poly([81, 85, 86], 'Hips')
poly([81, 82, 86], 'Hips')
poly([82, 86, 87], 'Hips')
poly([82, 83, 88], 'Hips')
poly([82, 87, 88], 'Hips')
poly([83, 84, 89], 'Hips')
poly([83, 88, 89], 'Hips')

poly([85, 86, 90], 'Hips')
poly([86, 90, 91], 'Hips')
poly([86, 87, 91], 'Hips')
poly([87, 91, 92], 'Hips')
poly([87, 88, 93], 'Hips')
poly([87, 92, 93], 'Hips')
poly([88, 89, 94], 'Hips')
poly([88, 93, 94], 'Hips')

poly([90, 91, 95], 'Hips')
poly([91, 95, 96], 'Hips')
poly([91, 92, 96], 'Hips')
poly([92, 96, 97], 'Hips')
poly([92, 93, 98], 'Hips')
poly([92, 97, 98], 'Hips')
poly([93, 94, 99], 'Hips')
poly([93, 98, 99], 'Hips')

# Groin split
poly([95, 96, 173], 'Hips')
poly([96, 97, 100], 'Hips')
poly([97, 98, 102], 'Hips')
poly([98, 99, 218], 'Hips')
poly([97, 100, 101], 'Hips')
poly([97, 101, 102], 'Hips')

# ============================================================
# LEFT UPPER ARM
# ============================================================
poly([56, 103, 104], 'Left Upper Arm')
poly([56, 61, 104], 'Left Upper Arm')
poly([103, 104, 105], 'Left Upper Arm')
poly([104, 105, 106], 'Left Upper Arm')
poly([105, 106, 107], 'Left Upper Arm')
poly([106, 107, 108], 'Left Upper Arm')
poly([107, 108, 109], 'Left Upper Arm')
poly([108, 109, 110], 'Left Upper Arm')
poly([109, 110, 111], 'Left Upper Arm')
poly([110, 111, 112], 'Left Upper Arm')
poly([111, 112, 113], 'Left Upper Arm')

# ============================================================
# LEFT FOREARM
# ============================================================
poly([111, 113, 114], 'Left Forearm')
poly([112, 113, 115], 'Left Forearm')
poly([113, 114, 115], 'Left Forearm')
poly([114, 115, 116], 'Left Forearm')
poly([115, 116, 117], 'Left Forearm')
poly([116, 117, 118], 'Left Forearm')
poly([117, 118, 119], 'Left Forearm')
poly([118, 119, 120], 'Left Forearm')
poly([119, 120, 121], 'Left Forearm')

# ============================================================
# LEFT HAND
# ============================================================
poly([120, 121, 122], 'Left Hand')
poly([121, 122, 123], 'Left Hand')
poly([122, 123, 124], 'Left Hand')
poly([122, 124, 125], 'Left Hand')
poly([123, 124, 126], 'Left Hand')
poly([124, 125, 127], 'Left Hand')
poly([124, 126, 127], 'Left Hand')
poly([122, 125, 128], 'Left Hand')
poly([128, 129, 125], 'Left Hand')
poly([125, 127, 131], 'Left Hand')
poly([131, 130, 125], 'Left Hand')
poly([127, 133, 132], 'Left Hand')
poly([127, 133, 135], 'Left Hand')
poly([135, 134, 127], 'Left Hand')
poly([126, 127, 137], 'Left Hand')
poly([137, 136, 126], 'Left Hand')

# ============================================================
# RIGHT UPPER ARM
# ============================================================
poly([57, 138, 139], 'Right Upper Arm')
poly([57, 63, 139], 'Right Upper Arm')
poly([138, 139, 140], 'Right Upper Arm')
poly([139, 140, 141], 'Right Upper Arm')
poly([140, 141, 142], 'Right Upper Arm')
poly([141, 142, 143], 'Right Upper Arm')
poly([142, 143, 144], 'Right Upper Arm')
poly([143, 144, 145], 'Right Upper Arm')
poly([144, 145, 146], 'Right Upper Arm')
poly([145, 146, 147], 'Right Upper Arm')
poly([146, 147, 148], 'Right Upper Arm')

# ============================================================
# RIGHT FOREARM
# ============================================================
poly([146, 148, 149], 'Right Forearm')
poly([147, 148, 150], 'Right Forearm')
poly([148, 149, 150], 'Right Forearm')
poly([149, 150, 151], 'Right Forearm')
poly([150, 151, 152], 'Right Forearm')
poly([151, 152, 153], 'Right Forearm')
poly([152, 153, 154], 'Right Forearm')
poly([153, 154, 155], 'Right Forearm')
poly([154, 155, 156], 'Right Forearm')

# ============================================================
# RIGHT HAND
# ============================================================
poly([155, 156, 157], 'Right Hand')
poly([156, 157, 158], 'Right Hand')
poly([157, 158, 159], 'Right Hand')
poly([157, 159, 160], 'Right Hand')
poly([158, 159, 161], 'Right Hand')
poly([159, 160, 162], 'Right Hand')
poly([159, 161, 162], 'Right Hand')
poly([157, 160, 163], 'Right Hand')
poly([163, 164, 160], 'Right Hand')
poly([160, 162, 166], 'Right Hand')
poly([166, 165, 160], 'Right Hand')
poly([162, 168, 167], 'Right Hand')
poly([162, 168, 170], 'Right Hand')
poly([170, 169, 162], 'Right Hand')
poly([161, 162, 172], 'Right Hand')
poly([172, 171, 161], 'Right Hand')

# ============================================================
# LEFT THIGH
# ============================================================
poly([95, 173, 174], 'Left Thigh')
poly([96, 100, 175], 'Left Thigh')
poly([95, 96, 175], 'Left Thigh')
poly([95, 173, 175], 'Left Thigh')
poly([173, 174, 175], 'Left Thigh')
poly([100, 175, 178], 'Left Thigh')
poly([174, 175, 176], 'Left Thigh')
poly([175, 176, 177], 'Left Thigh')
poly([175, 177, 178], 'Left Thigh')
poly([176, 177, 179], 'Left Thigh')
poly([177, 179, 180], 'Left Thigh')
poly([177, 178, 181], 'Left Thigh')
poly([177, 180, 181], 'Left Thigh')
poly([179, 180, 182], 'Left Thigh')
poly([180, 182, 183], 'Left Thigh')
poly([180, 181, 184], 'Left Thigh')
poly([180, 183, 184], 'Left Thigh')

# ============================================================
# LEFT KNEE
# ============================================================
poly([182, 183, 185], 'Left Thigh')
poly([183, 185, 186], 'Left Thigh')
poly([183, 184, 187], 'Left Thigh')
poly([183, 186, 187], 'Left Thigh')
poly([185, 186, 188], 'Left Thigh')
poly([186, 187, 188], 'Left Thigh')

# ============================================================
# LEFT SHIN
# ============================================================
poly([185, 188, 189], 'Left Calf')
poly([188, 189, 190], 'Left Calf')
poly([187, 188, 191], 'Left Calf')
poly([188, 190, 191], 'Left Calf')
poly([189, 190, 192], 'Left Calf')
poly([190, 192, 193], 'Left Calf')
poly([190, 191, 194], 'Left Calf')
poly([190, 193, 194], 'Left Calf')
poly([192, 193, 195], 'Left Calf')
poly([193, 195, 196], 'Left Calf')
poly([193, 194, 197], 'Left Calf')
poly([193, 196, 197], 'Left Calf')
poly([195, 196, 198], 'Left Calf')
poly([196, 198, 199], 'Left Calf')
poly([196, 197, 200], 'Left Calf')
poly([196, 199, 200], 'Left Calf')

# ============================================================
# LEFT ANKLE
# ============================================================
poly([198, 199, 201], 'Left Calf')
poly([199, 201, 202], 'Left Calf')
poly([199, 200, 203], 'Left Calf')
poly([199, 202, 203], 'Left Calf')

# ============================================================
# LEFT FOOT
# ============================================================
poly([201, 202, 204], 'Left Foot')
poly([202, 204, 205], 'Left Foot')
poly([202, 203, 206], 'Left Foot')
poly([202, 205, 206], 'Left Foot')
poly([204, 205, 207], 'Left Foot')
poly([205, 207, 208], 'Left Foot')
poly([205, 206, 209], 'Left Foot')
poly([205, 208, 209], 'Left Foot')
poly([207, 208, 210], 'Left Foot')
poly([208, 210, 211], 'Left Foot')
poly([208, 209, 212], 'Left Foot')
poly([208, 211, 212], 'Left Foot')
poly([210, 211, 213], 'Left Foot')
poly([211, 213, 214], 'Left Foot')
poly([211, 214, 215], 'Left Foot')
poly([211, 215, 216], 'Left Foot')
poly([211, 212, 216], 'Left Foot')
poly([212, 216, 217], 'Left Foot')

# ============================================================
# RIGHT THIGH
# ============================================================
poly([99, 218, 219], 'Right Thigh')
poly([98, 102, 220], 'Right Thigh')
poly([98, 99, 220], 'Right Thigh')
poly([99, 218, 220], 'Right Thigh')
poly([218, 219, 220], 'Right Thigh')
poly([102, 220, 223], 'Right Thigh')
poly([219, 220, 221], 'Right Thigh')
poly([220, 221, 222], 'Right Thigh')
poly([220, 222, 223], 'Right Thigh')
poly([221, 222, 224], 'Right Thigh')
poly([222, 224, 225], 'Right Thigh')
poly([222, 223, 226], 'Right Thigh')
poly([222, 225, 226], 'Right Thigh')
poly([224, 225, 227], 'Right Thigh')
poly([225, 227, 228], 'Right Thigh')
poly([225, 226, 229], 'Right Thigh')
poly([225, 228, 229], 'Right Thigh')

# ============================================================
# RIGHT KNEE
# ============================================================
poly([227, 228, 230], 'Right Thigh')
poly([228, 230, 231], 'Right Thigh')
poly([228, 229, 232], 'Right Thigh')
poly([228, 231, 232], 'Right Thigh')
poly([230, 231, 233], 'Right Thigh')
poly([231, 232, 233], 'Right Thigh')

# ============================================================
# RIGHT SHIN
# ============================================================
poly([230, 233, 234], 'Right Calf')
poly([233, 234, 235], 'Right Calf')
poly([232, 233, 236], 'Right Calf')
poly([233, 235, 236], 'Right Calf')
poly([234, 235, 237], 'Right Calf')
poly([235, 237, 238], 'Right Calf')
poly([235, 236, 239], 'Right Calf')
poly([235, 238, 239], 'Right Calf')
poly([237, 238, 240], 'Right Calf')
poly([238, 240, 241], 'Right Calf')
poly([238, 239, 242], 'Right Calf')
poly([238, 241, 242], 'Right Calf')
poly([240, 241, 243], 'Right Calf')
poly([241, 243, 244], 'Right Calf')
poly([241, 242, 245], 'Right Calf')
poly([241, 244, 245], 'Right Calf')

# ============================================================
# RIGHT ANKLE
# ============================================================
poly([243, 244, 246], 'Right Calf')
poly([244, 246, 247], 'Right Calf')
poly([244, 245, 248], 'Right Calf')
poly([244, 247, 248], 'Right Calf')

# ============================================================
# RIGHT FOOT
# ============================================================
poly([246, 247, 249], 'Right Foot')
poly([247, 249, 250], 'Right Foot')
poly([247, 248, 251], 'Right Foot')
poly([247, 250, 251], 'Right Foot')
poly([249, 250, 252], 'Right Foot')
poly([250, 252, 253], 'Right Foot')
poly([250, 251, 254], 'Right Foot')
poly([250, 253, 254], 'Right Foot')
poly([252, 253, 255], 'Right Foot')
poly([253, 255, 256], 'Right Foot')
poly([253, 254, 257], 'Right Foot')
poly([253, 256, 257], 'Right Foot')
poly([255, 256, 258], 'Right Foot')
poly([256, 258, 259], 'Right Foot')
poly([256, 259, 260], 'Right Foot')
poly([256, 260, 261], 'Right Foot')
poly([256, 257, 261], 'Right Foot')
poly([257, 261, 262], 'Right Foot')

# Torso-arm connections
poly([56, 64, 104], 'Upper Torso')
poly([57, 66, 139], 'Upper Torso')
poly([61, 64, 104], 'Upper Torso')
poly([63, 66, 139], 'Upper Torso')

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

# SVG
svg_lines = []
svg_lines.append('<?xml version="1.0" encoding="UTF-8"?>')
svg_lines.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 710" fill="none">')
svg_lines.append('  <style>')
svg_lines.append('    .facet { fill: none; stroke: #4a4a4a; stroke-width: 0.9; stroke-linejoin: round; }')
svg_lines.append('  </style>')

# Center symmetry line
svg_lines.append('  <line x1="350" y1="20" x2="350" y2="386" stroke="#ccc" stroke-width="0.3" stroke-dasharray="3,5"/>')

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

# HTML demo
html_svg = svg_content.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '')

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Low-Poly Female Front — Wireframe Topology</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400&family=Outfit:wght@200;300&display=swap');
  *{margin:0;padding:0;box-sizing:border-box}
  body{
    background:#fff;
    min-height:100vh;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    font-family:'Outfit',sans-serif;
    color:#333;
  }
  .page-wrapper{
    display:flex;
    flex-direction:column;
    align-items:center;
    padding:40px 20px 60px;
  }
  .title-block{
    text-align:center;
    margin-bottom:20px;
  }
  .title-block h1{
    font-family:'Cormorant Garamond',serif;
    font-weight:300;
    font-size:clamp(1.2rem,2.5vw,1.8rem);
    letter-spacing:0.15em;
    text-transform:uppercase;
    color:#555;
  }
  .title-block .subtitle{
    font-weight:200;
    font-size:0.65rem;
    letter-spacing:0.25em;
    text-transform:uppercase;
    color:#bbb;
    margin-top:4px;
  }
  .svg-container{
    width:clamp(340px,55vw,520px);
  }
  .svg-container svg{
    width:100%;
    height:auto;
    display:block;
  }
  .facet{
    fill:none;
    stroke:#4a4a4a;
    stroke-width:0.9;
    stroke-linejoin:round;
    transition:fill 0.2s ease, stroke 0.2s ease;
    cursor:pointer;
  }
  .facet:hover{
    fill:rgba(100,100,100,0.05);
    stroke:#333;
    stroke-width:1.1;
  }
  .facet.active{
    fill:rgba(80,80,80,0.08);
    stroke:#222;
    stroke-width:1.3;
  }
  .tooltip{
    position:fixed;
    pointer-events:none;
    background:rgba(255,255,255,0.96);
    border:1px solid #ddd;
    color:#666;
    font-weight:300;
    font-size:0.6rem;
    letter-spacing:0.1em;
    text-transform:uppercase;
    padding:4px 10px;
    border-radius:2px;
    opacity:0;
    transition:opacity 0.15s ease;
    z-index:100;
    white-space:nowrap;
  }
  .tooltip.visible{opacity:1}
  .footer-label{
    color:#ccc;
    font-size:0.5rem;
    letter-spacing:0.2em;
    text-transform:uppercase;
    margin-top:14px;
    font-weight:200;
  }
</style>
</head>
<body>
<div class="page-wrapper">
  <div class="title-block">
    <h1>Low-Poly Female &mdash; Front View</h1>
    <div class="subtitle">Wireframe Topology &bull; Beauty-Tech Series</div>
  </div>
  <div class="svg-container">
''' + html_svg + '''
  </div>
  <span class="footer-label">Hover to explore &bull; Click to select</span>
</div>
<div class="tooltip" id="tooltip"></div>
<script>
(function(){
  const tooltip = document.getElementById('tooltip');
  let active = null;
  document.querySelectorAll('.facet').forEach(f => {
    f.addEventListener('mouseenter', () => {
      tooltip.textContent = f.getAttribute('data-region');
      tooltip.classList.add('visible');
    });
    f.addEventListener('mousemove', e => {
      tooltip.style.left = (e.clientX + 12) + 'px';
      tooltip.style.top = (e.clientY - 8) + 'px';
    });
    f.addEventListener('mouseleave', () => tooltip.classList.remove('visible'));
    f.addEventListener('click', e => {
      e.stopPropagation();
      if(active) active.classList.remove('active');
      if(active === f){ active = null; return; }
      f.classList.add('active');
      active = f;
    });
  });
  document.addEventListener('click', () => {
    if(active){ active.classList.remove('active'); active = null; }
  });
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
print("\nFiles written successfully")
