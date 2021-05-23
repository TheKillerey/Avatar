#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    0x02137ded = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Lunar_Revel/Models/Dock_WaterReflection_A/Materials/Dock_WaterReflection_New2_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Normal_Texture"
                textureName: string = "ASSETS/Shared/Materials/Water_B_Nm.dds"
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/Dock_WaterReflection_A.TFT_ArenaSkin_LunarRevel.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Flow_Strength"
                value: vec4 = { 0.0299999993, 0.0299999993, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flow_Speed"
                value: vec4 = { 0.100000001, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flow_Direction"
            }
            StaticMaterialShaderParamDef {
                name: string = "Alpha"
                value: vec4 = { 0.409999996, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Normal_Tiling"
                value: vec4 = { 2, 0, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "ENABLE_LOW_QUALITY_ALPHA"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = 0xe5f58ac0
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    0xf678ef02 = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Lunar_Revel/Models/Dock_Flower_A/Materials/Dock_Lilypad_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/Dock_Lilypad_A.TFT_ArenaSkin_LunarRevel.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest_DoubleSided"
                        blendEnable: bool = true
                        cullEnable: bool = false
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    0x047404c8 = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Lunar_Revel/Materials/Default/Dock_LionStatue_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/Dock_LionStatue_A.TFT_ArenaSkin_LunarRevel.dds"
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
    0x53df5593 = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Lunar_Revel/Materials/Default/Dock_BreadAndButter_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/Dock_BreadandButter_A.TFT_ArenaSkin_LunarRevel.dds"
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
    0x5bad123d = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Lunar_Revel/Materials/Default/OD_Anatomy_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/OD_Anatomy_A.TFT_ArenaSkin_LunarRevel.dds"
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
    0xb60cc670 = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Lunar_Revel/Materials/Default/Board_OutsideDocks_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/Board_OutsideDocks_A.TFT_ArenaSkin_LunarRevel.dds"
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
    0xe8ebacd1 = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Lunar_Revel/Materials/Default/LR_T1_Brazier_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Lunar_Revel/Textures/LR_T1_Brazier_B.TFT_ArenaSkin_LunarRevel.dds"
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
    0x0a41a344 = MapPointLightType {
        lightColor: vec4 = { 0, 1, 0.784313738, 1 }
        radius: f32 = 950
        specular: bool = false
    }
    0x3b3506ed = MapPointLightType {
        lightColor: vec4 = { 0.905882359, 0.90196079, 0.854901969, 1 }
        Impact: i32 = 1
    }
    0xbea7d96e = MapPointLightType {
        lightColor: vec4 = { 0.905882359, 0.90196079, 0.854901969, 1 }
        Impact: i32 = 1
    }
    0x206a6f11 = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x050d0313 = 0xa783cfd5 {
                0x2a078c9c: string = "Play_sfx_tft_env_lunarrevel_outsidedock_amb_loop"
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Camera_Yellow"
                sceneLayer: string = "MapAudio"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2035.22791, -0.00048828125, 1935.02783, 1
                }
                name: string = "MapAudio_LunarRevel_OutsideDocks_Amb"
            }
            0x47d0e3f7 = 0xa783cfd5 {
                0x2a078c9c: string = "Play_sfx_tft_env_lunarrevel_outsidedock_water_west"
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Camera_Yellow"
                sceneLayer: string = "MapAudio"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1155.86279, 977.874756, 810.561768, 1
                }
                name: string = "MapAudio_LunarRevel_OutsideDocks_Water_West"
            }
            0x056c3b1a = 0xa783cfd5 {
                0x2a078c9c: string = "Play_sfx_tft_env_lunarrevel_outsidedock_water_east"
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Camera_Yellow"
                sceneLayer: string = "MapAudio"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3152.5, 111.337158, 1980.33545, 1
                }
                name: string = "MapAudio_LunarRevel_OutsideDocks_Water_East"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/Audio_OutsideDocks"
    }
    0x376c658c = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x280fc2be = null
            0xbd1c71ab = null
            0x0b9aca60 = null
            0xdcb0bca9 = null
            0x6d907bc4 = MapParticle {
                system: link = 0xe5d962fc
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1037.5293, 175.06752, 995.32489, 1
                }
                name: string = "TFT_LunarRevel_OutsideDocks_Braziers_Ocean1"
            }
            0x32226ce9 = MapParticle {
                system: link = 0xe5d962fc
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2883.95557, 175.06752, 995.32489, 1
                }
                name: string = "TFT_LunarRevel_OutsideDocks_Braziers_Ocean2"
            }
            0xf34f25a4 = MapParticle {
                system: link = 0xe5d962fc
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2965.46728, 165.440872, 3050.41821, 1
                }
                name: string = "TFT_LunarRevel_OutsideDocks_Braziers_Ocean3"
            }
            0x2ad2cd00 = MapParticle {
                system: link = 0xe5d962fc
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1119.04077, 165.440872, 3050.41821, 1
                }
                name: string = "TFT_LunarRevel_OutsideDocks_Braziers_Ocean4"
            }
            0x21dd19a0 = MapParticle {
                system: link = 0x545b95af
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3199.20898, -44.3678055, 1449.16931, 1
                }
                name: string = "TFT_LunarRevel_OutsideDocks_WaterCaustics_01_1"
            }
            0x956c5ec0 = MapParticle {
                system: link = 0x555b9742
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3291.86377, -46.1201172, 1962.66467, 1
                }
                name: string = "TFT_LunarRevel_OutsideDocks_WaterCaustics_02_1"
            }
            0x011a402b = MapParticle {
                system: link = 0x545b95af
                transform: mtx44 = {
                    0.56128788, 0, -0.827620625, 0
                    0, 1, 0, 0
                    0.827620625, 0, 0.56128788, 0
                    844.923523, -16.683342, 1494.79932, 1
                }
                name: string = "TFT_LunarRevel_OutsideDocks_WaterCaustics_01_2"
            }
            0xa30edca2 = MapParticle {
                system: link = 0x555b9742
                transform: mtx44 = {
                    -0.999989271, 0, -0.0047592991, 0
                    0, 1, 0, 0
                    0.0047592991, 0, -0.999989271, 0
                    666.501709, -22.8459473, 2026.7854, 1
                }
                name: string = "TFT_LunarRevel_OutsideDocks_WaterCaustics_02_2"
            }
            0xe9636956 = MapParticle {
                system: link = 0x545b95af
                transform: mtx44 = {
                    -0.637435555, 0, 0.7705037, 0
                    0, 1, 0, 0
                    -0.7705037, 0, -0.637435555, 0
                    3199.20898, -44.3678055, 2568.27686, 1
                }
                name: string = "TFT_LunarRevel_OutsideDocks_WaterCaustics_01_3"
            }
            0xf16a7c88 = MapParticle {
                system: link = 0x545b95af
                transform: mtx44 = {
                    -0.795853257, 0, -0.605490029, 0
                    0, 1, 0, 0
                    0.605490029, 0, -0.795853257, 0
                    841.590149, -24.5115204, 2564.7605, 1
                }
                name: string = "TFT_LunarRevel_OutsideDocks_WaterCaustics_01_4"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/Art_Shared"
    }
    0x41a2a14f = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xa570cb0c = MapLightingVolume {
                sunColor: vec4 = { 0.627451003, 0.533333361, 0.466666669, 1 }
                sunDirection: vec3 = { 0.25, 0.827000022, 0.300000012 }
                0xd8851203: f32 = 75
                0xba02f116: f32 = 0.150000006
                skyLightColor: vec4 = { 0.627451003, 0.533333361, 0.466666669, 1 }
                horizonColor: vec4 = { 0.478431374, 0.627451003, 0.384313732, 1 }
                groundColor: vec4 = { 0.372549027, 0.352941185, 0.627451003, 1 }
                skyLightScale: f32 = 0.600000024
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.580392182, 0.380392164, 0.278431386, 1 }
                fogAlternateColor: vec4 = { 0.0901960805, 0.164705887, 0.43921569, 1 }
                fogStartAndEnd: vec2 = { 500, -1100 }
                transform: mtx44 = {
                    1785.77222, 0, 0, 0
                    0, 5183.96924, 0, 0
                    0, 0, 1408.14478, 0
                    2000, 0, 2000, 1
                }
                name: string = "LightingVolume2"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/LightingVolume_OutsideDocks"
    }
    0x67dede8b = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xc83af5fe = null
            0x40199a64 = null
            0x4e0dc9a7 = null
            0x9d0e9812 = null
            0x01438c5e = null
            0x5b8088d6 = null
            0x13efd15a = null
            0x172ddfb8 = null
            0x030e8253 = null
            0x134e8a0f = null
            0x84d21eb8 = null
            0xe977dc9a = null
            0x547ebb4d = null
            0x3f336e68 = null
            0xd6f40609 = null
            0x8930d78b = null
            0x9adbeb35 = null
            0x7ddfe40a = null
            0xca0742a1 = null
            0xa95db54c = null
            0xceb79c97 = null
            0x2009e4cb = null
            0xb8a25af1 = null
            0xb2459569 = null
            0x84c602d2 = null
            0x4cc099db = null
            0xc67f15b4 = null
            0xd0fb7c3d = null
            0xb060a62c = null
            0xf3b19c39 = null
            0x574b7e75 = null
            0x4481769a = null
            0x25232b5c = null
            0x617251e6 = null
            0x944d4f16 = null
            0x35e19679 = null
            0x79a94651 = null
            0xac6b2fd1 = null
            0xb8e0820d = null
            0x9123f5e7 = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/Periph_OutsideDocks"
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
    0x77d159d3 = MapPlaceableContainer {
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/VFX_OutsideDocks"
    }
    0x9dbf579d = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x63b5d2a3 = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 0.999999881
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2872.74072, 317.165802, 2664.94604, 1
                }
                name: string = "SoftWhite_Point_Reality1"
            }
            0xdc7714bb = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 2.49065757
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2006.21106, 453.480011, 2043.24597, 1
                }
                name: string = "SoftWhite_Point_Reality8"
            }
            0x5e52b565 = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 1.31018806
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1144.53345, 317.165802, 1361.18225, 1
                }
                name: string = "SoftWhite_Point_Reality10"
            }
            0x16120e02 = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 1.31018806
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3061.23022, 317.165802, 1421.75732, 1
                }
                name: string = "SoftWhite_Point_Reality3"
            }
            0xac8e7b31 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.39199996
                intensityScale: f32 = 0.800000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1476.63232, 272.011353, 1148.76477, 1
                }
                name: string = "SoftWhite_Point_LunarCity1"
            }
            0x37c5c52e = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.39199996
                intensityScale: f32 = 0.800000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2500.15649, 272.011353, 1148.76477, 1
                }
                name: string = "SoftWhite_Point_LunarCity2"
            }
            0x36baa8df = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.39199996
                intensityScale: f32 = 0.800000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2002.14307, 272.011353, 1148.76477, 1
                }
                name: string = "SoftWhite_Point_LunarCity3"
            }
            0x836681be = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.39199996
                intensityScale: f32 = 0.800000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2002.14307, 272.011353, 2918.20142, 1
                }
                name: string = "SoftWhite_Point_LunarCity4"
            }
            0xfa8e4a55 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.39199996
                intensityScale: f32 = 0.800000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2500.15649, 272.011353, 2918.20142, 1
                }
                name: string = "SoftWhite_Point_LunarCity5"
            }
            0xca4decbb = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.39199996
                intensityScale: f32 = 0.800000012
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1476.63232, 272.011353, 2918.20142, 1
                }
                name: string = "SoftWhite_Point_LunarCity6"
            }
            0x5063eb1f = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 0.906116188
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1190.77405, 363.398529, 1770.38794, 1
                }
                name: string = "SoftWhite_Point_Reality2"
            }
            0x5bec17a1 = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 0.906116188
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1190.77405, 363.398529, 2264.38281, 1
                }
                name: string = "SoftWhite_Point_Reality5"
            }
            0xae446bd8 = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 0.906116188
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2823.90723, 363.398529, 2264.38281, 1
                }
                name: string = "SoftWhite_Point_Reality6"
            }
            0x695229a0 = MapPointLight {
                type: link = 0x3b3506ed
                radiusScale: f32 = 0.906116188
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2823.90723, 363.398529, 1770.38794, 1
                }
                name: string = "SoftWhite_Point_Reality7"
            }
            0x51bdf1cb = MapPointLight {
                type: link = 0x0a41a344
                radiusScale: f32 = 0.449999988
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2882.94189, 240.460007, 998.085022, 1
                }
                name: string = "Odyssey_LightTeal_Fill1"
            }
            0x04dbf66e = MapPointLight {
                type: link = 0x0a41a344
                radiusScale: f32 = 0.449999988
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1036.81494, 240.460007, 998.085022, 1
                }
                name: string = "Odyssey_LightTeal_Fill2"
            }
            0xdb0f52e6 = MapPointLight {
                type: link = 0x0a41a344
                radiusScale: f32 = 0.449999988
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1118.354, 240.460007, 3041.91699, 1
                }
                name: string = "Odyssey_LightTeal_Fill3"
            }
            0x36fb7ed2 = MapPointLight {
                type: link = 0x0a41a344
                radiusScale: f32 = 0.449999988
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2962.05396, 240.460007, 3041.91699, 1
                }
                name: string = "Odyssey_LightTeal_Fill4"
            }
            0xcb2c8af2 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.35455441
                intensityScale: f32 = 0.850000024
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1544.29785, -161.194885, 592.918274, 1
                }
                name: string = "SoftWhite_Point_LunarCity7"
            }
            0xc7762171 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.35500002
                intensityScale: f32 = 0.850000024
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2433.31641, -161.194885, 592.918274, 1
                }
                name: string = "SoftWhite_Point_LunarCity8"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/Lighting_OutsideDocks"
    }
    0xb88b536b = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xe3df2e49 = null
            0x717c5e54 = MapParticle {
                system: link = "Maps/Particles/TFT/TFT_Skybox"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000, 18.6369991, 2000, 1
                }
                name: string = "TFT_Skybox"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/Skybox_OutsideDocks"
    }
    0xe2d71a83 = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x18d482e6 = null
            0x429b11ac = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/LunarRevel/Board_OutsideDocks"
    }
    0x3e1380c9 = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/LunarRevel_OutsideDocks"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.701960802, 0.784313738, 0.839215696, 1 }
                sunDirection: vec3 = { -0.385433108, 0.828491211, -0.406255662 }
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
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/LunarRevel_OutsideDocks_Navgrid.aimesh_ngrid"
            }
            MapBakeProperties {
                0x22d24a9a: f32 = 1.10000002
                lightGridCharacterFullBrightIntensity: f32 = 0.5
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/LunarRevel_OutsideDocks/LightGrid.TFT_ArenaSkin_LunarRevel.dat"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            0x38c69e2e = 0x6fcb5e90
            0xd91d6ba8 = 0x67dede8b
            0x32991532 = 0x77d159d3
            0x36af605c = 0x41a2a14f
            0xe716d3d2 = 0xe2d71a83
            0x932ad854 = 0xb88b536b
            0xf6f37aec = 0x206a6f11
            0xb2559fda = 0x9dbf579d
            "Art_Shared" = 0x376c658c
        }
    }
    0x545b95af = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                emitterName: string = "WaterCausticx"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 0, -25 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 1 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 120, 1, 120 }
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
                                { 120, 1, 120 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 41
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_watercaustics_01.TFT_ArenaSkin_LunarRevel.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -8000
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -15, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_WaterCaustics_01.TFT_ArenaSkin_LunarRevel.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0700000003, -0.0700000003 }
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
                textureMult: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_WaterCaustics_01_Mult.TFT_ArenaSkin_LunarRevel.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0799999982, -0.180000007 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.0799999982, -0.180000007 }
                        }
                    }
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
        }
        particleName: string = "TFT_LunarRevel_OutsideDocks_WaterCaustics_01"
        particlePath: string = "Maps/Particles/TFT/LunarRevel/OutsideDocks/TFT_LunarRevel_OutsideDocks_WaterCaustics_01"
    }
    0x555b9742 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "WaterCausticx"
                importance: u8 = 0
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 0, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 1 }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 120, 1, 120 }
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
                                { 120, 1, 120 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 41
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_watercaustics_01.TFT_ArenaSkin_LunarRevel.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -8000
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 1, 3 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_WaterCaustics_01.TFT_ArenaSkin_LunarRevel.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0700000003, 0 }
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
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 1.5 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_WaterCaustics_01_Mult.TFT_ArenaSkin_LunarRevel.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.180000007, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1.5
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.180000007, 0 }
                        }
                    }
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
                    constantValue: vec2 = { 0.5, 1.5 }
                }
            }
        }
        particleName: string = "TFT_LunarRevel_OutsideDocks_WaterCaustics_02"
        particlePath: string = "Maps/Particles/TFT/LunarRevel/OutsideDocks/TFT_LunarRevel_OutsideDocks_WaterCaustics_02"
    }
    0xe5d962fc = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                emitterName: string = "BubbleConstant"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 25, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 1 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/DefaultColorOverlifetime.TFT_ArenaSkin_LunarRevel.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.576470613, 1, 0.839215696, 0.701960802 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.576470613, 1, 0.839215696, 0 }
                            { 0.576470613, 1, 0.839215696, 0.701960802 }
                            { 0.576470613, 1, 0.839215696, 0 }
                        }
                    }
                }
                pass: i16 = 10000
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 65, 55, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1.10000002, 1.10000002, 1.10000002 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_Shine.TFT_ArenaSkin_LunarRevel.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "Core"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 25, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 0, 0 }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 1 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/DefaultColorOverlifetime.TFT_ArenaSkin_LunarRevel.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.792156875, 0.960784316, 0.886274517, 0 }
                            { 0.0588235296, 0.882352948, 0.498039216, 0.819607854 }
                            { 0.0274509806, 0.278431386, 0.396078438, 0 }
                        }
                    }
                }
                pass: i16 = 7
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 150, 10 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 1.25, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_SoftCircle_02.TFT_ArenaSkin_LunarRevel.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "Shadow"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 25, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/DefaultColorOverlifetime.TFT_ArenaSkin_LunarRevel.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.650003791 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.454901963, 0.643137276, 0.662745118, 0 }
                            { 0.192156866, 0.87843138, 0.729411781, 0.298039228 }
                            { 0.105882354, 0.964705884, 0.53725493, 0 }
                        }
                    }
                }
                pass: i16 = 3
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 120, 10 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_SoftCircle_02.TFT_ArenaSkin_LunarRevel.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 2000
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 10
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 10
                            }
                            axisFraction: vec3 = { 1, 1, 1 }
                        }
                    }
                }
                emitterName: string = "WaterBubbles"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 70, 0 }
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
                                    0.699999988
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
                            { 0, 70, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 25, 12, 25 }
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
                                        0.200000003
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
                                { 25, 12, 25 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/DefaultColorOverlifetime.TFT_ArenaSkin_LunarRevel.dds"
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.215686277, 0.937254906, 1, 0.701960802 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0.215686277, 0.937254906, 1, 0 }
                            { 0.215686277, 0.937254906, 1, 0.701960802 }
                            { 0.215686277, 0.937254906, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.25
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
                            { 8, 8, 100 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.300000012, 0.300000012, 0.300000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_TinyBubble.TFT_ArenaSkin_LunarRevel.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Waterball"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 25, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_Ocean_Brazier_WaterBall.TFT_ArenaSkin_LunarRevel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.223529413, 0.611764729, 0.431372553, 1 }
                }
                pass: i16 = 6
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 0.0588235296, 0.827450991, 0.827450991, 1 }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        values: list[vec3] = {
                            { 0, 360, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.25, 1, 1 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_Waterfall_WhiteFalls_01.TFT_ArenaSkin_LunarRevel.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.349999994 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Shadow1"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/DefaultColorOverlifetime.TFT_ArenaSkin_LunarRevel.dds"
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0274509806, 0.152941182, 0.0784313753, 1 }
                }
                pass: i16 = 5
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 150, 10 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_Cloud_DrakePit_Distort_Tex.TFT_ArenaSkin_LunarRevel.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
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
                            3
                        }
                    }
                }
                emitterName: string = "Waterglob_01"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 45, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 25, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 25, 0 }
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
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 50, 25, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_Ocean_Brazier_Waterglob_01.TFT_ArenaSkin_LunarRevel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.858823538, 1, 0.984313726, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.227450982, 0.905882359, 0.65882355, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 6
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 0.0862745121, 0.97647059, 0.97647059, 0.870588243 }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        values: list[vec3] = {
                            { 360, 360, 360 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        values: list[vec3] = {
                            { 90, 90, 90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.64999998, 1, 1 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1.64999998, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_Waterfall_WhiteFalls_01.TFT_ArenaSkin_LunarRevel.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                                    0.699999988
                                    1
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
                emitterName: string = "Waterglob_2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 45, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 25, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 25, 0 }
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
                                        0
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 50, 25, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            360
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                        { 0, 0, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_Ocean_Brazier_Waterglob_01.TFT_ArenaSkin_LunarRevel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.858823538, 1, 0.984313726, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.20784314, 1, 0.643137276, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 6
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 0.0862745121, 0.97647059, 0.97647059, 0.870588243 }
                }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        values: list[vec3] = {
                            { 360, 360, 360 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 90 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        values: list[vec3] = {
                            { 90, 90, 90 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 1 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 2, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_Waterfall_WhiteFalls_01.TFT_ArenaSkin_LunarRevel.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Shadow2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/DefaultColorOverlifetime.TFT_ArenaSkin_LunarRevel.dds"
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.141176477, 0.0588235296, 0.247058824, 1 }
                }
                pass: i16 = 5
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 150, 10 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_Cloud_DrakePit_Distort_Tex.TFT_ArenaSkin_LunarRevel.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                emitterName: string = "Light"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 10, 0 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleColorTexture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/DefaultColorOverlifetime.TFT_ArenaSkin_LunarRevel.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.149996191 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.635294139, 1, 0.850980401, 0 }
                            { 0.0784313753, 1, 1, 1 }
                            { 0.184313729, 0.223529413, 1, 0 }
                        }
                    }
                }
                pass: i16 = 4
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 150, 10 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/LunarRevel/TFT_LunarRevel_OutsideDocks_Cloud_DrakePit_Distort_Tex.TFT_ArenaSkin_LunarRevel.dds"
            }
        }
        particleName: string = "TFT_LunarRevel_OutsideDocks_Braziers_Ocean"
        particlePath: string = "Maps/Particles/TFT/LunarRevel/OutsideDocks/TFT_LunarRevel_OutsideDocks_Braziers_Ocean"
        soundOnCreateDefault: string = "Play_sfx_Env_Map11_SRX_Brazier_Activate_buffactivate"
        soundPersistentDefault: string = "Play_sfx_Env_Map11_SRX_Ocean_Dragon_brazier"
        flags: u8 = 228
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
}
