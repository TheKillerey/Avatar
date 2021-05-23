#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    0x002072ad = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xf2de77f7 = MapParticle {
                system: link = "Maps/Particles/TFT/TFT_Skybox"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000, 18.6369991, 2000, 1
                }
                name: string = "TFT_Skybox"
            }
            0xe99ddc9b = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/Skybox_OutsideClub"
    }
    0x1e6a41fb = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xefc377e8 = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 1.31018806
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1088.98706, 317.165802, 1361.18225, 1
                }
                name: string = "SoftWhite_Point_Reality4"
            }
            0xd6426f8b = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 1.31018806
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2913.71338, 317.165802, 2667.19751, 1
                }
                name: string = "SoftWhite_Point_Reality9"
            }
            0x7a644bdf = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 2.49099994
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2006.21106, 453.480011, 2043.24597, 1
                }
                name: string = "SoftWhite_Point_LunarCity1"
            }
            0x97021a49 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.39199996
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2003.27295, 453.480011, 1121.15295, 1
                }
                name: string = "SoftWhite_Point_LunarCity2"
            }
            0xfbe5b863 = MapPointLight {
                type: link = 0x7d4509b7
                radiusScale: f32 = 1.57416284
                intensityScale: f32 = 1.64999998
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    961.563721, 497.0242, 1987.16992, 1
                }
                name: string = "Red_Point_Reality1"
            }
            0xf7775e09 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.39199996
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1479.13171, 453.480011, 1121.15295, 1
                }
                name: string = "SoftWhite_Point_LunarCity4"
            }
            0xa85898e8 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.39199996
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2500.59302, 453.480011, 1121.15295, 1
                }
                name: string = "SoftWhite_Point_LunarCity5"
            }
            0x9c8f762f = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.39199996
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2500.59302, 453.480011, 2938.07812, 1
                }
                name: string = "SoftWhite_Point_LunarCity3"
            }
            0x1e409d0b = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.39199996
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2003.27295, 453.480011, 2938.07812, 1
                }
                name: string = "SoftWhite_Point_LunarCity6"
            }
            0xa1818701 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.39199996
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1479.13171, 453.480011, 2938.07812, 1
                }
                name: string = "SoftWhite_Point_LunarCity7"
            }
            0xb8ef5ea9 = MapPointLight {
                type: link = 0xd5a4b3a5
                radiusScale: f32 = 1.00999999
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1040.21313, 240.460007, 998.43103, 1
                }
                name: string = "Light_Torch_01_1"
            }
            0x08026820 = MapPointLight {
                type: link = 0xd5a4b3a5
                radiusScale: f32 = 1.00999999
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2886.66479, 240.460007, 998.43103, 1
                }
                name: string = "Light_Torch_01_2"
            }
            0xacc545f7 = MapPointLight {
                type: link = 0xd5a4b3a5
                radiusScale: f32 = 1.00999999
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1118.36523, 240.460007, 3051.39868, 1
                }
                name: string = "Light_Torch_01_3"
            }
            0x2c97c532 = MapPointLight {
                type: link = 0xd5a4b3a5
                radiusScale: f32 = 1.00999999
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2965.30469, 240.460007, 3051.39868, 1
                }
                name: string = "Light_Torch_01_4"
            }
            0x7a4e69a1 = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 1.22504056
                intensityScale: f32 = 0.600000024
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1095.37891, 317.165802, 1927.54773, 1
                }
                name: string = "SoftWhite_Point_Reality1"
            }
            0xd57087ae = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 1.27867866
                intensityScale: f32 = 0.800000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2917.94043, 317.165802, 2145.84814, 1
                }
                name: string = "SoftWhite_Point_Reality2"
            }
            0x56510f02 = MapPointLight {
                type: link = 0x7d4509b7
                radiusScale: f32 = 1.29041839
                intensityScale: f32 = 0.800000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1550.39038, -141.906647, 555.174988, 1
                }
                name: string = "Red_Point_Reality2"
            }
            0xbae16de2 = MapPointLight {
                type: link = 0x7d4509b7
                radiusScale: f32 = 1.29041839
                intensityScale: f32 = 0.800000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2415.62744, -141.906647, 555.174988, 1
                }
                name: string = "Red_Point_Reality3"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/Lighting_OutsideClub"
    }
    0x2f06e387 = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x8355e65d = 0xa783cfd5 {
                0x2a078c9c: string = "Play_sfx_tft_env_lunarrevel_t1_common_crowd"
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Camera_Yellow"
                sceneLayer: string = "MapAudio"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    717.211487, 0, 2000, 1
                }
                name: string = "MapAudio_LunarRevel_T1_Common_Crowd"
            }
            0xb3bbe3de = 0xa783cfd5 {
                0x2a078c9c: string = "Play_sfx_tft_env_lunarrevel_outsideclub_beat"
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Camera_Yellow"
                sceneLayer: string = "MapAudio"
                transform: mtx44 = {
                    0.99999994, 0, 0, 0
                    0, 0.99999994, 0, 0
                    0, 0, 0.999999881, 0
                    1013.05756, 0, 2000, 1
                }
                name: string = "MapAudio_LunarRevel_OutsideClub_Club"
            }
            0xea0fc2f0 = 0xa783cfd5 {
                0x2a078c9c: string = "Play_sfx_tft_env_lunarrevel_outsideclub_amb_loop"
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Camera_Yellow"
                sceneLayer: string = "MapAudio"
                transform: mtx44 = {
                    0.99999994, 0, 0, 0
                    0, 0.99999994, 0, 0
                    0, 0, 0.999999881, 0
                    2003.63306, 0, 2000, 1
                }
                name: string = "MapAudio_LunarRevel_OutsideClub_Amb"
            }
            0xb37a1124 = 0xa783cfd5 {
                0x2a078c9c: string = "Play_sfx_tft_env_lunarrevel_outsideclub_footsteps"
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Camera_Yellow"
                sceneLayer: string = "MapAudio"
                transform: mtx44 = {
                    0.99999994, 0, 0, 0
                    0, 0.99999994, 0, 0
                    0, 0, 0.999999881, 0
                    3073.23291, 0, 2036.71704, 1
                }
                name: string = "MapAudio_LunarRevel_OutsideClub_Footsteps"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/Audio_OutsideClub"
    }
    0x6fcb5e90 = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xf7e857de = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Spawn_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2915.95557, 11.2485962, 2462.1416, 1
                }
                name: string = "GoldMineLocatorAway"
            }
            0x9b9787df = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1103.59802, 11.2485962, 1615.37769, 1
                }
                name: string = "GoldMineLocator"
            }
            0x4bff90c5 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2801, 0, 2911.16626, 1
                }
                name: string = "BenchAwayLocator"
            }
            0x90883f04 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1203.64636, 0, 1140.53381, 1
                }
                name: string = "BenchHomeLocator"
            }
            0x4cb64046 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2957.82544, 0, 2927.14917, 1
                }
                name: string = "ItemBenchAwayLocator"
            }
            0x1cd3dd02 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1042.78552, 0, 1122.86438, 1
                }
                name: string = "ItemBenchLocator"
            }
            0x2f580834 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1421.01526, 0, 1458, 1
                }
                name: string = "BoardLocator"
            }
            0x717bb0ac = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1956.11304, 0, 1628.69995, 1
                }
                name: string = "Camera_Island"
            }
            0xf874b8e7 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    -1, -8.74227766e-08, 0, 0
                    -8.74227766e-08, 1, -8.74227766e-08, 0
                    7.64274186e-15, -8.74227766e-08, -1, 0
                    2067, 0, 2427.01318, 1
                }
                name: string = "Camera_Flipped_Island"
            }
            0xe9d84b9b = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1187.76733, 0, 1388.43628, 1
                }
                name: string = "PerchLocator"
            }
            0x58f4606b = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2832.14062, 0, 2664.4563, 1
                }
                name: string = "PerchAwayLocator"
            }
            0xe1404aa4 = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Generic_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000, 0, 2000, 1
                }
                name: string = "BoardCenterLocator"
            }
            0xc723a0b3 = MapCamera {
                0x563a1941: f32 = 3700
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2056.11304, 0, 1700.69995, 1
                }
                name: string = "Camera_TFT_IslandHome_PC"
            }
            0xd0ce0321 = MapCamera {
                0x563a1941: f32 = 3700
                yaw: f32 = 180
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1967, 0, 2355, 1
                }
                name: string = "Camera_TFT_IslandAway_PC"
            }
            0x7fd48cc3 = MapCamera {
                0x6f3e4327: f32 = 1200
                0x563a1941: f32 = 3180
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1956.11304, 0, 1920.69995, 1
                }
                name: string = "Camera_TFT_IslandHome_Mobile"
            }
            0xb9b64b31 = MapCamera {
                0x6f3e4327: f32 = 1200
                0x563a1941: f32 = 3180
                yaw: f32 = 180
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2067, 0, 2135, 1
                }
                name: string = "Camera_TFT_IslandAway_Mobile"
            }
            0x608bfae5 = MapCamera {
                0x563a1941: f32 = 4500
                pitch: f32 = 41
                FieldOfView: f32 = 55
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2056.11304, 0, 1700.69995, 1
                }
                name: string = "Camera_TFT_StoreView"
            }
            0x2e12e907 = MapCamera {
                0x563a1941: f32 = 4500
                pitch: f32 = 89.9000015
                FieldOfView: f32 = 55
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2056.11304, 100, 1700.69995, 1
                }
                name: string = "Camera_TFT_StoreThumb"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/LunarRevel_Design_Base_3"
    }
    0xa6dbe74d = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x194bcce8 = null
            0x8dbaf9d8 = null
            0x86bb9ca7 = null
            0xa863b5bb = null
            0x10d37369 = null
            0x2ec7c5b7 = null
            0xc443ef0b = null
            0x1145cb05 = null
            0xb04c3d54 = null
            0x054e71f8 = null
            0x5e58ffc4 = MapParticle {
                system: link = 0x9db5f7a7
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2880.85181, 159.040039, 1012.9649, 1
                }
                name: string = "TFT_BrazierFire_A1"
            }
            0x7d942d8c = MapParticle {
                system: link = 0x9db5f7a7
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1035.53931, 159.040039, 1012.9649, 1
                }
                name: string = "TFT_BrazierFire_A2"
            }
            0xff22bb69 = MapParticle {
                system: link = 0x9db5f7a7
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1116.78992, 159.040039, 3057.00244, 1
                }
                name: string = "TFT_BrazierFire_A3"
            }
            0x3411a7c8 = MapParticle {
                system: link = 0x9db5f7a7
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2962.10254, 159.040039, 3057.00244, 1
                }
                name: string = "TFT_BrazierFire_A4"
            }
            0xfb5fe606 = MapParticle {
                system: link = 0x174b7795
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    720.679565, -4.62252808, 1976.61487, 1
                }
                name: string = "TFT_LunarRevel_OutsideClub_DoorLight_01_1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/Periph_OutsideClub"
    }
    0xbe375d85 = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x6fe60d19 = null
            0x81d430eb = null
            0xb7926c41 = null
            0xa7ef4937 = null
            0x99f9b11e = null
            0xb44b36ab = null
            0x6bbf4ea1 = null
            0x053e2b3e = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/Board_OutsideClub"
    }
    0xcefda5f5 = MapPlaceableContainer {
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/VFX_OutsideClub"
    }
    0xd124f7a9 = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xd2aceaa7 = MapLightingVolume {
                sunColor: vec4 = { 0.627451003, 0.498039216, 0.592156887, 1 }
                sunDirection: vec3 = { 0.25, 0.827000022, 0.300000012 }
                0xd8851203: f32 = 75
                0xba02f116: f32 = 0.150000006
                skyLightColor: vec4 = { 0.53725493, 0.627451003, 0.43921569, 1 }
                horizonColor: vec4 = { 0.627451003, 0.592156887, 0.384313732, 1 }
                groundColor: vec4 = { 0.356862754, 0.376470596, 0.627451003, 1 }
                skyLightScale: f32 = 0.829999983
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.521568656, 0.301960796, 0.250980407, 1 }
                fogAlternateColor: vec4 = { 0.105882354, 0.380392164, 0.698039234, 1 }
                fogStartAndEnd: vec2 = { 500, -1200 }
                transform: mtx44 = {
                    1576.79199, 0, 0, 0
                    0, 5183.96924, 0, 0
                    0, 0, 1350.3324, 0
                    2000, 0, 2000, 1
                }
                name: string = "LightingVolume1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/LightingVolume_OutsideClub"
    }
    0xc4034d5f = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/LunarRevel_OutsideClub"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.701960802, 0.784313738, 0.839215696, 1 }
                sunDirection: vec3 = { -0.476804554, 0.789230764, -0.387004048 }
                0xd8851203: f32 = 75
                skyLightColor: vec4 = { 0.454901963, 0.631372571, 0.741176486, 1 }
                horizonColor: vec4 = { 0.274509817, 0.419607848, 0.509803951, 1 }
                groundColor: vec4 = { 0.450980395, 0.568627477, 0.650980413, 1 }
                skyLightScale: f32 = 1.5
                fogEnabled: bool = false
                fogColor: vec4 = { 0.100007631, 0.059998475, 0.110002287, 1 }
                fogAlternateColor: vec4 = { 0.420004576, 0.379995435, 0.420004576, 1 }
                fogStartAndEnd: vec2 = { -1000, -20000 }
                fogEmissiveRemap: f32 = 1
                useBloom: bool = true
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.899999976
            }
            MapNavGrid {
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/LunarRevel_OutsideClub_Navgrid.aimesh_ngrid"
            }
            MapBakeProperties {
                0x22d24a9a: f32 = 1.10000002
                lightGridCharacterFullBrightIntensity: f32 = 0.5
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/LunarRevel_OutsideClub/LightGrid.TFT_ArenaSkin_LunarRevel.dat"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            0x38c69e2e = 0x6fcb5e90
            0x07ea164e = 0xcefda5f5
            0x21537e14 = 0x002072ad
            0x539e36cc = 0x2f06e387
            0xc0c92a96 = 0x1e6a41fb
            0x0bb497dc = 0xd124f7a9
            0x07a26240 = 0xa6dbe74d
            0x16ffba6e = 0xbe375d85
        }
    }
    0x3a45416f = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Lunar_Revel/Models/Paper_Lantern_A/Materials/ENV_Lantern_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/Club2_PaperLantern_A.TFT_ArenaSkin_LunarRevel.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/Club2_PaperLantern_Mask_A.dds"
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Size"
                value: vec4 = { 3.52945018, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Dodge_MinValue"
                value: vec4 = { 0.502499998, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Dodge_MaxValue"
                value: vec4 = { 0.805000007, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flicker_Rate"
                value: vec4 = { 0.875, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_AXIS_OFFSET_VALUE"
                value: vec4 = { 10, -2, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "SPEED_RANDOMIZER_VALUE"
                value: vec4 = { 2.5, 0.5, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_VERTEX_ANIMATION"
            }
        }
        shaderMacros: map[string,string] = {
            "NO_BAKED_LIGHTING" = "1"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_Lantern"
                        cullEnable: bool = false
                    }
                }
            }
        }
        0xe251b20a: bool = false
    }
    0x230acbde = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Lunar_Revel/Materials/Default/Board_OutsideClub_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/Board_OutsideClub_A.TFT_ArenaSkin_LunarRevel.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    0x256510a1 = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Lunar_Revel/Materials/Default/Lunar_Revel_T1_BaseCliff_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/Lunar_Revel_T1_BaseCliff.TFT_ArenaSkin_LunarRevel.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    0x54f5118c = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Lunar_Revel/Materials/Default/LR_T1_Brazier_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/LR_T1_Brazier_A.TFT_ArenaSkin_LunarRevel.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    0x6ee343f0 = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Lunar_Revel/Materials/Default/OC_Anatomy_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/OC_Anatomy_A.TFT_ArenaSkin_LunarRevel.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    0x95b5cffb = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Lunar_Revel/Materials/Default/OC_Sidewalk_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/OC_Sidewalk_A.TFT_ArenaSkin_LunarRevel.dds"
                addressW: u32 = 1
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Materials/Default/Default/Skybox_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Default/Default/Skybox_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Default/TFT_Skybox2.dds"
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Shared/Materials/white.dds"
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Scroll_Speed"
                value: vec4 = { 0.00499999989, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Rotation_Speed"
                value: vec4 = { 0.0500000007, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Color_Blend"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Color_Multiply"
                value: vec4 = { 1, 1, 1, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "TOGGLE_UV_ROTATE_SCROLL"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "TOGGLE_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_COLOR_BLEND"
                on: bool = false
            }
        }
        shaderMacros: map[string,string] = {
            "NO_BAKED_LIGHTING" = "1"
            "DISABLE_DEPTH_FOG" = "1"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/TFT_Skybox"
                    }
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Materials/Default/Default/Skybox_B_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Default/Default/Skybox_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Default/TFT_Skybox_Bottom_2b.dds"
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Shared/Materials/white.dds"
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Scroll_Speed"
                value: vec4 = { 0.0500000007, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Rotation_Speed"
                value: vec4 = { 0.0500000007, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Color_Blend"
                value: vec4 = { 0.5, 0.5, 0.5, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Color_Multiply"
                value: vec4 = { 1, 1, 1, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "TOGGLE_UV_ROTATE_SCROLL"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "TOGGLE_MASK"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_COLOR_BLEND"
                on: bool = false
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/TFT_Skybox"
                        shaderMacros: map[string,string] = {
                            "NO_BAKED_LIGHTING" = "1"
                            "DISABLE_DEPTH_FOG" = "1"
                        }
                    }
                }
            }
        }
    }
    0x174b7795 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "FloorLight_Add"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.149996191 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.862745106, 1, 1 }
                            { 1, 0.725490212, 1, 1 }
                            { 1, 0.619607866, 0.850980401, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 150, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_City_Glow_01.TFT_ArenaSkin_LunarRevel.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    5
                }
                emitterName: string = "FloorLight_Alpha"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.300007641, 0.39000535, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0419847332
                            0.106870227
                            0.162213743
                            0.618320644
                            0.744274795
                            0.874045789
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.207034305 }
                            { 1, 1, 1, 0.728971958 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.803738356 }
                            { 1, 1, 1, 0.186915889 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 300, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_Club_Glow_03.TFT_ArenaSkin_LunarRevel.dds"
                textureMult: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_Club_Base_SmokeErode.TFT_ArenaSkin_LunarRevel.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    5
                }
                emitterName: string = "FloorFog"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 175, 10, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.749996185 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.179995418, 0.349996179, 0.669993162, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0419847332
                            0.106870227
                            0.162213743
                            0.618320644
                            0.744274795
                            0.874045789
                            1
                        }
                        values: list[vec4] = {
                            { 0.179995418, 0.349996179, 0.669993162, 0 }
                            { 0.179995418, 0.349996179, 0.669993162, 0.207034305 }
                            { 0.179995418, 0.349996179, 0.669993162, 0.728971958 }
                            { 0.179995418, 0.349996179, 0.669993162, 1 }
                            { 0.179995418, 0.349996179, 0.669993162, 1 }
                            { 0.179995418, 0.349996179, 0.669993162, 0.803738356 }
                            { 0.179995418, 0.349996179, 0.669993162, 0.186915889 }
                            { 0.179995418, 0.349996179, 0.669993162, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 25
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 350, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideBalcony_Vertical_Glow.TFT_ArenaSkin_LunarRevel.dds"
                texAddressModeBase: u8 = 2
                textureMult: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideBalcony_Unitcombination_Backdrop_Mult.TFT_ArenaSkin_LunarRevel.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0 }
                        }
                    }
                }
                uvScaleMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1.5, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    5
                }
                emitterName: string = "DoorLight_Add"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 300, -115 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.100007631 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec4] = {
                            { 0.996078432, 0.80392158, 1, 1 }
                            { 1, 0.549996197, 1, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 4
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 25
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 350, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideBalcony_Vertical_Glow.TFT_ArenaSkin_LunarRevel.dds"
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    5
                }
                emitterName: string = "DoorFog"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 165, 300, -200 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.179995418, 0.349996179, 0.669993162, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0419847332
                            0.106870227
                            0.162213743
                            0.618320644
                            0.744274795
                            0.874045789
                            1
                        }
                        values: list[vec4] = {
                            { 0.179995418, 0.349996179, 0.669993162, 0 }
                            { 0.179995418, 0.349996179, 0.669993162, 0.207034305 }
                            { 0.179995418, 0.349996179, 0.669993162, 0.728971958 }
                            { 0.179995418, 0.349996179, 0.669993162, 1 }
                            { 0.179995418, 0.349996179, 0.669993162, 1 }
                            { 0.179995418, 0.349996179, 0.669993162, 0.803738356 }
                            { 0.179995418, 0.349996179, 0.669993162, 0.186915889 }
                            { 0.179995418, 0.349996179, 0.669993162, 0 }
                        }
                    }
                }
                pass: i16 = 5
                alphaRef: u8 = 0
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 350, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideBalcony_Vertical_Glow.TFT_ArenaSkin_LunarRevel.dds"
                texAddressModeBase: u8 = 2
                textureMult: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideBalcony_Unitcombination_Backdrop_Mult.TFT_ArenaSkin_LunarRevel.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                uvScaleMult: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 0.75 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    5
                }
                emitterName: string = "DoorFog_Alpha1"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 300, -115 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.300007641, 0.39000535, 0.349996179 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0419847332
                            0.106870227
                            0.162213743
                            0.618320644
                            0.744274795
                            0.874045789
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.207034305 }
                            { 1, 1, 1, 0.728971958 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.803738356 }
                            { 1, 1, 1, 0.186915889 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 3
                alphaRef: u8 = 0
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 350, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideBalcony_Vertical_Glow.TFT_ArenaSkin_LunarRevel.dds"
                texAddressModeBase: u8 = 2
                textureMult: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_Club_Base_SmokeErode.TFT_ArenaSkin_LunarRevel.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                uvScaleMult: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 0.75 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.949999988
                                    1.04999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    5
                }
                emitterName: string = "DoorRays"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 300, -115 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.530006886, 0.62999922, 0.700007617 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0419847332
                            0.106870227
                            0.162213743
                            0.618320644
                            0.744274795
                            0.874045789
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.207034305 }
                            { 1, 1, 1, 0.728971958 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.803738356 }
                            { 1, 1, 1, 0.186915889 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 6
                alphaRef: u8 = 0
                uvScrollAlphaMult: flag = false
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 350, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideClub_Rays_01.TFT_ArenaSkin_LunarRevel.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0500000007, 0 }
                }
                texAddressModeBase: u8 = 2
                textureMult: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideClub_Rays_01.TFT_ArenaSkin_LunarRevel.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0370000005, 0 }
                }
            }
        }
        particleName: string = "TFT_LunarRevel_OutsideClub_DoorLight_01"
        particlePath: string = "Maps/Particles/TFT/LunarRevel/OutsideClub/TFT_LunarRevel_OutsideClub_DoorLight_01"
    }
    0x9db5f7a7 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.75
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Fire"
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { -200, 500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -200, 500, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 10, 10 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 10, 10, 10 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 48
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -180
                                    180
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 80, 80 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 80, 80 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.300000012, 0.600000024, 0.600000024 }
                            { 0.5, 1, 1 }
                            { 0.300000012, 0.600000024, 0.600000024 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_flipbook_01.SRI_Slots.dds"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
                textureMult: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_mult.SRI_Slots.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1.25 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                texDivMult: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                emitterName: string = "baseGlow"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 49
                alphaRef: u8 = 0
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 60, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_glow.TFT_Set4.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.8000002
                }
                emitterName: string = "sparks"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0.400000006, 0.400000006, 0.400000006 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0.400000006, 0.400000006 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 200, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 0.600000024, 0.600000024 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 25, 15, 25 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 25, 15, 25 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 45
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 48
                colorLookUpTypeY: u8 = 3
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 15, 15, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 0.5, 0 }
                            { 0.200000003, 0.200000003, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_Ash_01.TFT_Set4.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.25
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.25
                        }
                    }
                }
                emitterName: string = "Smoke"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -20, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 5, 5, 5 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 5, 5, 5 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.269993126, 0.269993126, 0.269993126, 0.62999922 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.269993126, 0.269993126, 0.269993126, 0.62999922 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.458823532, 0, 0, 0.239215687 }
                            { 0.992156863, 0, 0, 1 }
                            { 0.459998488, 0, 0, 0.450003803 }
                            { 0.113725491, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 46
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/TFT_Smoke_Erosion.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -80
                                    80
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                directionVelocityScale: f32 = 0.00200000009
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 80, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 80, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.200000003, 0.600000024 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Base_Sl_Dust_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "baseGlow1"
                blendMode: u8 = 4
                pass: i16 = 50
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 1, 1 }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_glow.TFT_Set4.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    10.1999998
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "ground_glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                pass: i16 = 80
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 340, 340 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Ground_Glow.TFT_Set5.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "mouth_flame_R3"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 30, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                pass: i16 = 47
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { 1, 3.0999999 }
                disableBackfaceCull: bool = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 60, 50 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/MonkeyKing_Skin05_I_flame_anim.TFT_1105.dds"
                frameRate: f32 = 40
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
        }
        particleName: string = "TFT_BrazierFire_A"
        particlePath: string = "Maps/Particles/TFT/LunarRevel/OutsideBalcony/TFT_BrazierFire_A"
        soundPersistentDefault: string = "Play_sfx_tft_env_lunarrevel_t1_common_fire"
        flags: u8 = 197
        systemScale: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
    }
    "Maps/Particles/TFT/TFT_Skybox" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "TFT_Skybox_Bot"
                disabled: bool = true
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Particles/TFT_Default_Skybox1.scb"
                    }
                }
                blendMode: u8 = 1
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                texture: string = "ASSETS/Particles/TFT_Default_Skybox1.dds"
                scaleOverride: vec3 = { 18, 18, 18 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "TFT_Skybox_Walls"
                disabled: bool = true
                importance: u8 = 2
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Particles/TFT_Default_Skybox2.scb"
                    }
                }
                blendMode: u8 = 1
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                texture: string = "ASSETS/Particles/TFT_Default_Skybox2.dds"
                scaleOverride: vec3 = { 18, 18, 18 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Clouds_A"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -500, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Cloud_A.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.62999922 }
                }
                pass: i16 = -9997
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.0199999996, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.20000005, 1.20000005, 1.20000005 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 1 }
                }
                texture: string = "ASSETS/Particles/TFT_Skybox2_Floaters.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0149999997, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Clouds_B"
                importance: u8 = 2
                translationOverride: vec3 = { 1, -1, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -500, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Cloud_B.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                pass: i16 = -9997
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1, 1 }
                }
                texture: string = "ASSETS/Particles/TFT_Skybox2_Floaters.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00999999978, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/TFT_Cloud_Mult.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0500000007, 0 }
                }
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                scaleOverride: vec3 = { 16, 16, 16 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.00499999989
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.400000006
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.400000006
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            -1
                        }
                    }
                }
                isSingleParticle: flag = true
                emitterName: string = "Wind"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -450, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Wind.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.90196079, 0.788235307, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.603921592, 0.254901975, 1 }
                }
                pass: i16 = -9999
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Env_TFT_Skybox_Wind.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.699999988
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.100000001
                                    0.100000001
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.100000001, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0 }
                        }
                    }
                }
                uvTransformCenter: vec2 = { 1, 1 }
                scaleOverride: vec3 = { 17.5, 17.5, 17.5 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.129999995
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                lifetime: option[f32] = {
                    100000
                }
                emitterName: string = "Clouds_A_Thunder"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -550, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Cloud_A.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0524475537
                            0.0909090936
                            0.141608387
                            0.279720277
                            0.307692319
                            0.442307681
                            0.472027957
                            0.604895115
                            0.674825191
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.300007641 }
                            { 1, 1, 1, 0.0233015642 }
                            { 1, 1, 1, 0.300007641 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.294182241 }
                            { 1, 1, 1, 0.0145634776 }
                            { 1, 1, 1, 0.154372856 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.14563477 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -9999
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.0199999996, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.60000002, 1.60000002, 1.60000002 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.20000005, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Skybox2_Floaters_Mask.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0149999997, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/TFT_Skybox2_Floaters_Mask_Mult.dds"
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 3
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.129999995
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                lifetime: option[f32] = {
                    100000
                }
                emitterName: string = "Clouds_B_Thunder"
                importance: u8 = 2
                translationOverride: vec3 = { 1, -1, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -500, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Cloud_B.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.00349650346
                            0.0506993011
                            0.113636367
                            0.157342657
                            0.279720277
                            0.307692319
                            0.433566421
                            0.604895115
                            0.627622366
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.378640771 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.621359229 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.980582535 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.281553388 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -9996
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Skybox2_Floaters_Mask.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0149999997, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/TFT_Skybox2_Floaters_Mask_Mult.dds"
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                scaleOverride: vec3 = { 16, 16, 16 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                emitterName: string = "TFT_Skybox_WallsL"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -65, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Whole.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0524475537
                            0.0909090936
                            0.141608387
                            0.279720277
                            0.307692319
                            0.442307681
                            0.472027957
                            0.604895115
                            0.674825191
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.300007641 }
                            { 1, 1, 1, 0.0233015642 }
                            { 1, 1, 1, 0.300007641 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.294182241 }
                            { 1, 1, 1, 0.0145634776 }
                            { 1, 1, 1, 0.154372856 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.14563477 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -9998
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 4
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Default_Skybox2_Mask.dds"
                textureMult: string = "ASSETS/Maps/Particles/TFT/TFT_Skybox2_Floaters_Mask_Mult.dds"
                birthUVOffsetMult: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                scaleOverride: vec3 = { 18, 18, 18 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Clouds_A1"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -450, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/Skybox_Cloud_A.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.62999922 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.827450991, 0.894117653, 1 }
                }
                pass: i16 = -9997
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.0799999982, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.20000005, 1.20000005, 1.20000005 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.5, 1 }
                }
                texture: string = "ASSETS/Particles/TFT_Skybox2_Floaters.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.00300000003, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 1 }
                }
                scaleOverride: vec3 = { 17, 17, 17 }
            }
        }
        visibilityRadius: f32 = 12000
        particleName: string = "TFT_Skybox"
        particlePath: string = "Maps/Particles/TFT/TFT_Skybox"
        flags: u8 = 197
    }
    0x3b3506ed = MapPointLightType {
        lightColor: vec4 = { 0.905882359, 0.90196079, 0.854901969, 1 }
        Impact: i32 = 1
    }
    0x7d4509b7 = MapPointLightType {
        lightColor: vec4 = { 1, 0, 0.0156862754, 1 }
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0xbea7d96e = MapPointLightType {
        lightColor: vec4 = { 0.905882359, 0.90196079, 0.854901969, 1 }
        Impact: i32 = 1
    }
    0xd5a4b3a5 = MapPointLightType {
        lightColor: vec4 = { 1, 0.552941203, 0.188235298, 1 }
        radius: f32 = 450
        specular: bool = false
    }
}
