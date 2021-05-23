#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Maps/KitPieces/TFT/Materials/Freljord/Custom/BattleField_WintersClaw_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Custom/BattleField_WintersClaw_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Board_A.TFT_Freljord.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Mask_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Board_A_Mask.TFT_Freljord.dds"
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Diffuse_Offset"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Factor"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_Color"
                value: vec4 = { 0.23137255, 0.533333361, 0.564705908, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Diffuse_Color"
                value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Bounds"
                value: vec4 = { 0, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Frequency"
                value: vec4 = { 10, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Speed"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Scroll_Speed"
                value: vec4 = { -1.39999998, 1.20000005, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Frequency"
                value: vec4 = { 2.8499999, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Glow_Opacity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Radial_Glow_Opacity"
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_SmoothStep"
                value: vec4 = { 0, 1.10000002, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Glow_Intensity_Min_Max"
                value: vec4 = { 0.150000006, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "UV_Rotation"
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_DIFFUSE_COLOR"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_RADIAL_GLOW"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_UV_SCROLL_GLOW"
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_GLOW"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "TOGGLE_UV_DIRECTION"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_GLOW_AS_ALPHA"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_GLOW_MASK"
            }
            StaticMaterialSwitchDef {
                name: string = "RADIAL_UV_LOCALSPACE_TOGGLE"
                on: bool = false
            }
        }
        shaderMacros: map[string,string] = {
            "DISABLE_DEPTH_FOG" = "1"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Glow"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        dynamicMaterial: pointer = DynamicMaterialDef {}
    }
    "Maps/KitPieces/TFT/Materials/Freljord/Custom/Banner_Wind_Statue_WintersClaw_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Custom/Banner_Wind_Statue_WintersClaw_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Banners_A.TFT_Freljord.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Time_Multiplier_Y_Axis"
                value: vec4 = { -1, 0.75, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Offset_Frequency"
                value: vec4 = { 5, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Offset_Low"
                value: vec4 = { -1.26999998, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Offset_High"
                value: vec4 = { 1.40999997, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_Vertex_Displacement"
                value: vec4 = { 0, -2, -4, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Time_Multiplier_Z_Axis"
                value: vec4 = { -0.600000024, 0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Offset_Frequency"
                value: vec4 = { 15, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Offset_Low"
                value: vec4 = { -2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Offset_High"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_Vertex_Displacement"
                value: vec4 = { -8, -17, 0.75, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Time_Multiplier_X_Axis"
                value: vec4 = { -0.600000024, 1.20000005, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Offset_Frequency"
                value: vec4 = { 18, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Offset_Low"
                value: vec4 = { -1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Offset_High"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_Vertex_Displacement"
                value: vec4 = { 10, 2, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Rotation"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Rotation"
                value: vec4 = { 74.6999969, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Rotation"
            }
            StaticMaterialShaderParamDef {
                name: string = "X_UV_Mask_Distance_Offset"
                value: vec4 = { -0.300000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Mask_Low"
                value: vec4 = { 0.300000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Mask_High"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_UV_Mask_Distance_Offset"
                value: vec4 = { -0.0599999987, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Mask_Low"
                value: vec4 = { 0.200000003, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Mask_High"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_UV_Mask_Distance_Offset"
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Mask_Low"
                value: vec4 = { 0.00999999978, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Mask_High"
                value: vec4 = { 0.639999986, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Wind_Global_Intensity"
                value: vec4 = { 3, 1, 120, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_Offset_UV_Wave"
                value: vec4 = { 1, 0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_Offset_UV_Wave"
                value: vec4 = { 0.5, 0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_Offset_UV_Wave"
                value: vec4 = { 0.5, 1, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_X_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Y_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Z_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_X_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_Y_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_Z_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Y_AXIS_UV_MASK_DIRECTION_TOGGLE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "X_AXIS_UV_MASK_DIRECTION_TOGGLE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Z_AXIS_UV_MASK_DIRECTION_TOGGLE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_X_AXIS_UV_MASK"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Y_AXIS_UV_MASK"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Z_AXIS_UV_MASK"
            }
            StaticMaterialSwitchDef {
                name: string = "X_AXIS_UV_MASK_DIRECTION_INVERT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Y_AXIS_UV_MASK_DIRECTION_INVERT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Z_AXIS_UV_MASK_DIRECTION_INVERT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_UV_MASK_X_AXIS"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_UV_MASK_Y_AXIS"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_UV_MASK_Z_AXIS"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_REMOVE_ALPHA"
                on: bool = false
            }
        }
        shaderMacros: map[string,string] = {
            "DISABLE_DEPTH_FOG" = "1"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/TFT_VertexWave"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        dynamicMaterial: pointer = DynamicMaterialDef {
            parameters: list[embed] = {
                DynamicMaterialParameterDef {
                    name: string = "Wind_Global_Intensity"
                    enabled: bool = false
                    driver: pointer = TimeMaterialDriver {}
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Materials/Freljord/Custom/Banner_Wind_WintersClaw_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Custom/Banner_Wind_WintersClaw_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Flags_A.TFT_Freljord.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Time_Multiplier_Y_Axis"
                value: vec4 = { -1, 0.75, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Offset_Frequency"
                value: vec4 = { 5, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Offset_Low"
                value: vec4 = { -1.26999998, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Offset_High"
                value: vec4 = { 1.40999997, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_Vertex_Displacement"
                value: vec4 = { 0, -2, -4, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Time_Multiplier_Z_Axis"
                value: vec4 = { -0.600000024, 0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Offset_Frequency"
                value: vec4 = { 15, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Offset_Low"
                value: vec4 = { -2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Offset_High"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_Vertex_Displacement"
                value: vec4 = { -8, -17, 0.75, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Time_Multiplier_X_Axis"
                value: vec4 = { -0.850000024, 1.20000005, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Offset_Frequency"
                value: vec4 = { 18, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Offset_Low"
                value: vec4 = { -1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Offset_High"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_Vertex_Displacement"
                value: vec4 = { 20, 32, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Rotation"
                value: vec4 = { 0.899999976, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Rotation"
                value: vec4 = { 74.6999969, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Rotation"
            }
            StaticMaterialShaderParamDef {
                name: string = "X_UV_Mask_Distance_Offset"
                value: vec4 = { -0.219999999, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Mask_Low"
                value: vec4 = { 0.25, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_UV_Mask_High"
                value: vec4 = { 0.800000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_UV_Mask_Distance_Offset"
                value: vec4 = { -0.0599999987, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Mask_Low"
                value: vec4 = { 0.200000003, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_UV_Mask_High"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_UV_Mask_Distance_Offset"
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Mask_Low"
                value: vec4 = { 0.00999999978, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_UV_Mask_High"
                value: vec4 = { 0.639999986, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Wind_Global_Intensity"
                value: vec4 = { 5, 1, 120, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "X_Axis_Offset_UV_Wave"
                value: vec4 = { 1, 0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Y_Axis_Offset_UV_Wave"
                value: vec4 = { 0.5, 0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Z_Axis_Offset_UV_Wave"
                value: vec4 = { 0.5, 1, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_X_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Y_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Z_OFFSET"
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_X_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_Y_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_Z_OFFSET"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Y_AXIS_UV_MASK_DIRECTION_TOGGLE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "X_AXIS_UV_MASK_DIRECTION_TOGGLE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Z_AXIS_UV_MASK_DIRECTION_TOGGLE"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_X_AXIS_UV_MASK"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Y_AXIS_UV_MASK"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_Z_AXIS_UV_MASK"
            }
            StaticMaterialSwitchDef {
                name: string = "X_AXIS_UV_MASK_DIRECTION_INVERT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Y_AXIS_UV_MASK_DIRECTION_INVERT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "Z_AXIS_UV_MASK_DIRECTION_INVERT"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_UV_MASK_X_AXIS"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_UV_MASK_Y_AXIS"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_VIEW_UV_MASK_Z_AXIS"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEBUG_REMOVE_ALPHA"
                on: bool = false
            }
        }
        shaderMacros: map[string,string] = {
            "DISABLE_DEPTH_FOG" = "1"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/TFT_VertexWave"
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        dynamicMaterial: pointer = DynamicMaterialDef {
            parameters: list[embed] = {
                DynamicMaterialParameterDef {
                    name: string = "Wind_Global_Intensity"
                    enabled: bool = false
                    driver: pointer = TimeMaterialDriver {}
                }
            }
        }
    }
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Brazier_Base_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Brazier_Base_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Brazier_Base_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Doorway_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Doorway_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Doorway_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Opponent_Side_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Opponent_Side_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Opponent_Side_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Keystone_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Keystone_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Keystone_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Bench_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Bench_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Bench_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Opponent_Side_B_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Opponent_Side_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Opponent_Side_B.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Column_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Column_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Column_A.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Skybox_Bottom_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Skybox_Bottom_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/TFT_Freljord_Skybox_Bottom.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Wood_Beam_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Wood_Beam_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Wood_Beam_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Flag_Stand_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Flag_Stand_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Flag_Stand_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Statue_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Statue_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Statue_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Bridge_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Bridge_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Bridge_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Small_Props_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Small_Props_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Small_Props_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Staircase_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Staircase_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Staircase_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Fortress_B_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Fortress_B_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Fortress_B.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Skybox_Side_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Skybox_Side_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/TFT_Freljord_Skybox_Side.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Glaciers_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Glaciers_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Glaciers_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Rocks_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Rocks_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Rocks_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Fortress_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Fortress_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Fortress_A.TFT_Freljord.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Default/Chain_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Default/Chain_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Chain_A.dds"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Alpha/Snow_Banks_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Alpha/Snow_Banks_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Snow_Banks_A.TFT_Freljord.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.00499999989, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Alpha/Flags_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Alpha/Flags_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/Flags_A.TFT_Freljord.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.00499999989, 0, 0, 0 }
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
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
    "Maps/KitPieces/TFT/Materials/Freljord/Alpha/SnowIcicles_Alphas_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Materials/Freljord/Alpha/SnowIcicles_Alphas_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/textures/Freljord/SnowIcicles_Alphas_A.TFT_Freljord.dds"
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
                        shader: link = "Shaders/Environment/DefaultEnv_Flat_AlphaTest"
                        blendEnable: bool = true
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
    }
    "Maps/KitPieces/Howling_Abyss/Materials/lambert4181_inst" = StaticMaterialDef {
        name: string = "Maps/KitPieces/Howling_Abyss/Materials/lambert4181_inst"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/Howling_Abyss/textures/Prop_Brazier_2.dds"
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
    "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Snow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 150
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldNoiseDefinitions: list[embed] = {
                        VfxFieldNoiseDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 4000
                            }
                            frequency: embed = ValueFloat {
                                constantValue: f32 = 30
                            }
                            velocityDelta: embed = ValueFloat {
                                constantValue: f32 = 150
                            }
                            axisFraction: vec3 = { 1, 1, 1 }
                        }
                    }
                }
                emitterName: string = "Snow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1000, -300, 1000 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1000, -300, 1000 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1200, 1600, 1200 }
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
                                { 1200, 1600, 1200 }
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
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
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
                                    0.300000012
                                    1
                                }
                            }
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
                    constantValue: vec4 = { 0.719996929, 0.949996173, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.719996929, 0.949996173, 1, 0 }
                            { 0.719996929, 0.949996173, 1, 0.600000024 }
                            { 0.719996929, 0.949996173, 1, 0 }
                        }
                    }
                }
                pass: i16 = 200
                isDirectionOriented: flag = true
                directionVelocityScale: f32 = 0.00200000009
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 0 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Firefly_Mote.TFT_Set5.dds"
                uvMode: u8 = 2
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "TFT_Freljord_WintersClaw_Snow"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Snow"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Cast" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 5000
        particleName: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Cast"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Cast"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_wintersclaw_heavywinds_cast"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_WintersClaw" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Fire"
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 750, 0 }
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
                            { 500, 750, 0 }
                        }
                    }
                }
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 15, 15 }
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
                                { 15, 15, 15 }
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.725490212, 0.725490212, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.250980407, 0.0666666701, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.250980407, 0.0666666701, 0 }
                            { 1, 0.250980407, 0.0666666701, 1 }
                            { 1, 0.250980407, 0.0666666701, 0.800000012 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
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
                texture: string = "ASSETS/Maps/Particles/TFT/Env_MB_brazierFire_flipbook_01.TFT_1105.dds"
                numFrames: u16 = 8
                texDiv: vec2 = { 4, 2 }
                textureMult: string = "ASSETS/Maps/Particles/TFT/Env_MB_brazierFire_mult2.dds"
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
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
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
                            1
                        }
                    }
                }
                emitterName: string = "Glow"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.725490212, 0.725490212, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.400000006, 0.200000003, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.400000006, 0.200000003, 0 }
                            { 1, 0.400000006, 0.200000003, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 60, 0 }
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
                            { 50, 60, 0 }
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
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/TFT_Varus/Skins/Base/Particles/bigglow02.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.449999988
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
                            0.449999988
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Fire1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 0, 300 }
                }
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
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.725490212, 0.725490212, 1 }
                }
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
                            { 1, 1, 1, 0.500007629 }
                            { 0, 0, 0.498039216, 0 }
                        }
                    }
                }
                pass: i16 = 1
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
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/TFT_Dust_Erosion.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
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
                    constantValue: vec3 = { 100, 80, 80 }
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
                            { 100, 80, 80 }
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
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
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
                            1
                        }
                    }
                }
                emitterName: string = "Smoke1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 100, 0 }
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
                            { 150, 100, 0 }
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
                pass: i16 = -10
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
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
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
                            0.5
                        }
                    }
                }
                emitterName: string = "baseGlow1"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.725490212, 0.725490212, 1 }
                }
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
                pass: i16 = 2
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 60, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 60, 0 }
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
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_glow.TFT_Set4.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
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
                                    1
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
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
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
                            1
                        }
                    }
                }
                emitterName: string = "baseGlow2"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.725490212, 0.725490212, 1 }
                }
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
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 60, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 60, 0 }
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
                            { 0.100000001, 0.100000001, 0 }
                            { 1, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_brazierFire_glow.TFT_Set4.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            6
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
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
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.1999998
                }
                emitterName: string = "ground_glow"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.725490212, 0.725490212, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.647058845, 0.576470613, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.647058845, 0.576470613, 0 }
                            { 1, 0.647058845, 0.576470613, 1 }
                            { 1, 0.647058845, 0.576470613, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 340, 340 }
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
                            { 150, 340, 340 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Ground_Glow.TFT_Set5.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
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
                            1
                        }
                    }
                }
                emitterName: string = "mouth_flame_R"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 45, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 0 }
                }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 15, 0 }
                    }
                }
                blendMode: u8 = 1
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
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -2
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { 1, 3 }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 70, 50 }
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
                            { 70, 70, 50 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/MonkeyKing_Skin05_I_flame_anim.TFT_1105.dds"
                frameRate: f32 = 40
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
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
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    10.8000002
                }
                emitterName: string = "sparks2"
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
                    constantValue: vec3 = { 500, 100, 500 }
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
                            { 500, 100, 500 }
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.725490212, 0.725490212, 1 }
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
                            { 0, 0, 0.498039216, 0 }
                        }
                    }
                }
                pass: i16 = 1
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
        }
        particleName: string = "TFT_Freljord_BrazierFire_WintersClaw"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_WintersClaw"
        flags: u8 = 197
        systemScale: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Edge_Flurries" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
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
                            4
                        }
                    }
                }
                emitterName: string = "longWind"
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 500, 0, 0 }
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
                                        1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 500, 0, 0 }
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
                                            0.166600004
                                            0.166700006
                                            0.5
                                            0.500100017
                                            0.666599989
                                            0.666700006
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
                                            180
                                            180
                                            270
                                            270
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
                                            0.5
                                            0.500100017
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Flurry_Wind_Mesh.TFT_Freljord.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.530006886 }
                }
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
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -90, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 7, 3, 5 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Flurry_Wind.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.20000005
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
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
                            4
                        }
                    }
                }
                emitterName: string = "wipeWind"
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
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
                                        1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
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
                                            0.166600004
                                            0.166700006
                                            0.5
                                            0.500100017
                                            0.666599989
                                            0.666700006
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
                                            180
                                            180
                                            270
                                            270
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
                                            0.5
                                            0.500100017
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Flurry_Wind_Wave_Mesh.TFT_Freljord.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.689997733 }
                }
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
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -90, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Flurry_Wind_Wave.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.400000006, -0.400000006 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.400000006, -0.400000006 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
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
                            4
                        }
                    }
                }
                emitterName: string = "longWind1"
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 20, 100, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 100 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                                { 0, 0, 100 }
                            }
                        }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Flurry_Wind_Mesh.TFT_Freljord.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.510002315 }
                }
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
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 140, 90, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 7, 3, 2 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Flurry_Wind.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 3, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 3, 0 }
                        }
                    }
                }
            }
        }
        particleName: string = "TFT_Freljord_WintersClaw_Edge_Flurries"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Edge_Flurries"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Fog" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
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
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Wind"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 1, 4000 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -500
                                        0
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
                                { 0, 1, 4000 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds_Mesh.TFT_Freljord.sco"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.809994638 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.549019635, 0.843137264, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.549019635, 0.843137264, 1, 0 }
                            { 0.549019635, 0.843137264, 1, 1 }
                            { 0.549019635, 0.843137264, 1, 1 }
                            { 0.549019635, 0.843137264, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 800
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 80, 80 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 60, 80, 80 }
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
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0149999997, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.0149999997, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
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
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
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
                            10
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "WindDark"
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -200, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 1, 4000 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -500
                                        0
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
                                { 0, 1, 4000 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds_Mesh.TFT_Freljord.sco"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.459998488 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.650980413, 0.909803927, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.650980413, 0.909803927, 1, 0 }
                            { 0.650980413, 0.909803927, 1, 1 }
                            { 0.650980413, 0.909803927, 1, 1 }
                            { 0.650980413, 0.909803927, 1, 0 }
                        }
                    }
                }
                pass: i16 = 49
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 800
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 80, 80 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 60, 80, 80 }
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
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0149999997, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.0149999997, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
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
            }
        }
        visibilityRadius: f32 = 8000
        particleName: string = "TFT_Freljord_WintersClaw_Fog"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Fog"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Godrays" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.449999988
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 7
                }
                particleLinger: option[f32] = {
                    17
                }
                emitterName: string = "Godray"
                disabled: bool = true
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 900, 0, 1 }
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
                                { 900, 0, 1 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_Godrays_Mesh.TFT_Freljord.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.470588237, 0.949019611, 1, 0 }
                            { 0.411764711, 0.717647076, 1, 1 }
                            { 0.325490206, 0.41568628, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaRef: u8 = 0
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.899999976
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_GodRays.TFT_Freljord.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.0500000007
                                    0.0500000007
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.25, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLinger: option[f32] = {
                    20
                }
                emitterName: string = "Godray1"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 600, 0, 600 }
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
                                { 600, 0, 600 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_GodRay.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.360784322, 0.647058845, 1, 1 }
                }
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
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2, 2 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_GodRays.TFT_Freljord.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -0.0500000007
                                    0.0500000007
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.25, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 0 }
                        }
                    }
                }
            }
        }
        visibilityRadius: f32 = 1000
        particleName: string = "TFT_Freljord_WintersClaw_Godrays"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Godrays"
        flags: u8 = 132
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Fire" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Fire"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Fire"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_wintersclaw_fire_bright_loop"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Wind" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 13
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
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
                            13
                        }
                    }
                }
                emitterName: string = "Wind"
                importance: u8 = 0
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Wind_Mesh.TFT_Freljord.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.549996197 }
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.549996197 }
                        }
                    }
                }
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
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 60
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 1, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 1, 30 }
                        }
                    }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Wind_Wisp.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.5, 0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                                    -0.100000001
                                    0.100000001
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.5, 0.5 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
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
                textureMult: string = "ASSETS/Maps/Particles/TFT/TFT_Unitcombination_Backdrop_Mult.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
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
                            { -0.100000001, 0.100000001 }
                        }
                    }
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
            }
        }
        visibilityRadius: f32 = 6000
        particleName: string = "TFT_Freljord_WintersClaw_Wind"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Wind"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Cloth_Flaps_Loop" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Cloth_Flaps_Loop"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Cloth_Flaps_Loop"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_wintersclaw_cloth_flapping_loop"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Air_Loop" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 3000
        particleName: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Air_Loop"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Air_Loop"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_wintersclaw_air_loop"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Structure_Crumble_Distant" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 3000
        particleName: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Structure_Crumble_Distant"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Structure_Crumble_Distant"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_wintersclaw_structure_crumble_distant"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Flurries" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.349999994
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
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
                            4
                        }
                    }
                }
                emitterName: string = "longWind"
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 500, 0, 0 }
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
                                        1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 500, 0, 0 }
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
                                            0.166600004
                                            0.166700006
                                            0.5
                                            0.500100017
                                            0.666599989
                                            0.666700006
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
                                            180
                                            180
                                            270
                                            270
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
                                            0.5
                                            0.500100017
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Flurry_Wind_Mesh.TFT_Freljord.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.570000768 }
                }
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
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -90, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 7, 3, 5 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Flurry_Wind.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.850000024, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.850000024, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.519999981
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.519999981
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
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
                            4
                        }
                    }
                }
                emitterName: string = "wipeWind"
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 50, 0 }
                    }
                    emitOffset: embed = ValueVector3 {
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
                                        1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
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
                                            0.166600004
                                            0.166700006
                                            0.5
                                            0.500100017
                                            0.666599989
                                            0.666700006
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
                                            180
                                            180
                                            270
                                            270
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
                                            0.5
                                            0.500100017
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Flurry_Wind_Wave_Mesh.TFT_Freljord.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.689997733 }
                }
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
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -90, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/TFT_Freljord_Flurry_Wind_Wave.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.400000006, -0.400000006 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.400000006, -0.400000006 }
                        }
                    }
                }
            }
        }
        particleName: string = "TFT_Freljord_WintersClaw_Flurries"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Flurries"
    }
    "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Edge_Fog" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
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
                                    0.800000012
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
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Wind"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
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
                                        1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
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
                                            0.166600004
                                            0.166700006
                                            0.5
                                            0.500100017
                                            0.666599989
                                            0.666700006
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
                                            180
                                            180
                                            270
                                            270
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
                                            0.5
                                            0.500100017
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds_Mesh.TFT_Freljord.sco"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.489997715 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.549019635, 0.843137264, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.549019635, 0.843137264, 1, 0 }
                            { 0.549019635, 0.843137264, 1, 1 }
                            { 0.549019635, 0.843137264, 1, 1 }
                            { 0.549019635, 0.843137264, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.5
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/TFT_Smoke_Erosion.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    10
                                    -10
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 10, 10 }
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
                        values: list[vec3] = {
                            { 30, 10, 10 }
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
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.800000012, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.800000012, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
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
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.200000003
                        }
                    }
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
                                    0.800000012
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
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "WindDark"
                shape: embed = VfxShape {
                    emitOffset: embed = ValueVector3 {
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
                                        1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
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
                                            0.166600004
                                            0.166700006
                                            0.5
                                            0.500100017
                                            0.666599989
                                            0.666700006
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
                                            180
                                            180
                                            270
                                            270
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
                                            0.5
                                            0.500100017
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0
                                            0
                                            90
                                            90
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds_Mesh.TFT_Freljord.sco"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.340001523 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.650003791, 0.910002291, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.650003791, 0.910002291, 1, 0 }
                            { 0.650003791, 0.910002291, 1, 0.600000024 }
                            { 0.650003791, 0.910002291, 1, 0.600000024 }
                            { 0.650003791, 0.910002291, 1, 0 }
                        }
                    }
                }
                pass: i16 = 49
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 100
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.5
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Maps/Particles/TFT/TFT_Smoke_Erosion.TFT_Set5.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    10
                                    -10
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 10, 10 }
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
                        values: list[vec3] = {
                            { 30, 10, 10 }
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
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/TFT_Freljord_AbyssClouds.TFT_Freljord.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.5, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { -0.5, 0 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
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
            }
        }
        visibilityRadius: f32 = 8000
        particleName: string = "TFT_Freljord_WintersClaw_Edge_Fog"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Edge_Fog"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Loop" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 3000
        particleName: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Loop"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Loop"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_wintersclaw_heavywinds_loop"
    }
    "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Lantern_Squeaks_Loop" = VfxSystemDefinitionData {
        simpleEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                particleLinger: option[f32] = {
                    10
                }
                emitterName: string = "empty"
                particleColorTexture: string = "ASSETS/Shared/Particles/Black.DDS"
                meshRenderFlags: u8 = 0
                texture: string = "ASSETS/Shared/Particles/Black.DDS"
                birthScale1: embed = ValueFloat {
                    constantValue: f32 = 0
                }
            }
        }
        visibilityRadius: f32 = 2000
        particleName: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Lantern_Squeaks_Loop"
        particlePath: string = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Lantern_Squeaks_Loop"
        soundPersistentDefault: string = "Play_sfx_tft_env_freljord_wintersclaw_lantern_squeaks_loop"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Lighting_WintersClaw" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xb4f0704f = MapPointLight {
                type: link = 0xf449b3ec
                radiusScale: f32 = 0.72052747
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2976.91772, 417.737, 922.216431, 1
                }
                name: string = "Light_Orange5"
            }
            0x8bd917dc = MapPointLight {
                type: link = 0xf449b3ec
                radiusScale: f32 = 0.720527947
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1031.5769, 417.737, 3021.98486, 1
                }
                name: string = "Light_Orange6"
            }
            0x2ec45dd5 = MapPointLight {
                type: link = 0xe25bb04b
                radiusScale: f32 = 1.99999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3236.52881, 57.0727844, 4645.18604, 1
                }
                name: string = "Light_Blue8"
            }
            0xe5a3255b = MapPointLight {
                type: link = 0xf449b3ec
                radiusScale: f32 = 0.720528007
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1042.21826, 417.737, 927.106445, 1
                }
                name: string = "Light_Orange7"
            }
            0x23d75586 = MapPointLight {
                type: link = 0xf402c51c
                radiusScale: f32 = 0.5910905
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1062.13855, 542.281067, 1425.30664, 1
                }
                name: string = "Light_White5"
            }
            0xfbf98a2d = MapPointLight {
                type: link = 0xf449b3ec
                radiusScale: f32 = 0.720527887
                intensityScale: f32 = 1.70000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2968.73242, 417.737, 3029.87109, 1
                }
                name: string = "Light_Orange8"
            }
            0x5ae84016 = MapPointLight {
                type: link = 0xe25bb04b
                radiusScale: f32 = 1.99999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    814.515869, 57.0727844, 4645.18604, 1
                }
                name: string = "Light_Blue10"
            }
            0xddaaf47a = MapPointLight {
                type: link = 0xf402c51c
                radiusScale: f32 = 0.591090798
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2848.76709, 541.888733, 2502.06689, 1
                }
                name: string = "Light_White8"
            }
            0x8fc5f891 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 1.49999619
                intensityScale: f32 = 2
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2025.87781, -846.201782, 1144.92163, 1
                }
                name: string = "Light_DarkBlue1"
            }
            0xaa4c1e64 = MapPointLight {
                type: link = 0x925f06fe
                radiusScale: f32 = 0.977619529
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1558.30127, 612.253052, 2358.94824, 1
                }
                name: string = "light_38_1"
            }
            0x244d86a6 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 1.49999833
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    962.295166, -474.081787, 3981.07471, 1
                }
                name: string = "Light_DarkBlue5"
            }
            0xe0f6e72c = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 1.49999881
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2807.03711, -474.081787, 4422.94189, 1
                }
                name: string = "Light_DarkBlue2"
            }
            0xbb748039 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 1.49999702
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -139.079529, -474.081787, 2840.33521, 1
                }
                name: string = "Light_DarkBlue3"
            }
            0x1e8dde3e = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 1.49999487
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1066.94116, -473.450928, -82.4660645, 1
                }
                name: string = "Light_DarkBlue6"
            }
            0xa7a78947 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 1.49999452
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3534.01904, -474.081787, -82.4660645, 1
                }
                name: string = "Light_DarkBlue7"
            }
            0xceac9bf0 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 1.49999309
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3994.29443, -474.081787, 1599.28967, 1
                }
                name: string = "Light_DarkBlue8"
            }
            0x311a682f = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 1.49999261
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3956.88867, -474.081787, 2912.90063, 1
                }
                name: string = "Light_DarkBlue9"
            }
            0xed317da5 = MapPointLight {
                type: link = 0xf449b3ec
                radiusScale: f32 = 1.00562072
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3666.98657, -335.597076, 2166.30396, 1
                }
                name: string = "Light_Orange1"
            }
            0x07ece84e = MapPointLight {
                type: link = 0xf449b3ec
                radiusScale: f32 = 1.00562119
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    416.67511, -335.597076, 2176.43262, 1
                }
                name: string = "Light_Orange2"
            }
            0x82a36234 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.49999994
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3303.65576, -203.972687, 2162.23218, 1
                }
                name: string = "Light_DarkBlue10"
            }
            0x49766daf = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.49999994
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3448.59863, 227.122864, 2851.76807, 1
                }
                name: string = "Light_DarkBlue11"
            }
            0x42d9ccc5 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.49999994
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    642.40094, -203.972321, 2148.56738, 1
                }
                name: string = "Light_DarkBlue12"
            }
            0x36c9a409 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.49999994
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2780.18213, 63.1950684, 3927.5835, 1
                }
                name: string = "Light_DarkBlue13"
            }
            0x34f32ebd = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.49999994
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3080.54761, 452.113647, 3519.75122, 1
                }
                name: string = "Light_DarkBlue14"
            }
            0x01eccd47 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.49999994
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    258.703125, -370.967957, 742.548706, 1
                }
                name: string = "Light_DarkBlue15"
            }
            0x1c7cbdb3 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.49999994
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3645.0625, -211.999939, 972.099243, 1
                }
                name: string = "Light_DarkBlue16"
            }
            0x9af0f62b = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.49999994
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    151.010315, -645.463379, 1865.20264, 1
                }
                name: string = "Light_DarkBlue17"
            }
            0x301002f2 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.49999994
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4147.85156, -952.941528, 2272.44043, 1
                }
                name: string = "Light_DarkBlue18"
            }
            0x08658f2b = MapPointLight {
                type: link = 0xe25bb04b
                radiusScale: f32 = 1.05790186
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2041.84363, -450.41095, 331.189758, 1
                }
                name: string = "Light_Blue2"
            }
            0xd413b97c = MapPointLight {
                type: link = 0x925f06fe
                radiusScale: f32 = 0.977619529
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2430.11621, 612.253052, 2358.94824, 1
                }
                name: string = "light_38_2"
            }
            0xaded6ab3 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.54774648
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2007.03247, 247.725067, 790.869019, 1
                }
                name: string = "Light_DarkBlue4"
            }
            0x72ed9626 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.165165111
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1248.97266, 153.429962, 912.685242, 1
                }
                name: string = "Light_DarkBlue19"
            }
            0x01923f1f = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.0912297517
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1663.23792, 45.8941345, 959.549316, 1
                }
                name: string = "Light_DarkBlue20"
            }
            0x74af0e14 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.136159897
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2733.17041, 98.5271988, 858.0625, 1
                }
                name: string = "Light_DarkBlue21"
            }
            0x1c0c15db = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.0691072047
                intensityScale: f32 = 0.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2865.73657, 58.8991776, 741.194702, 1
                }
                name: string = "Light_DarkBlue22"
            }
            0x9d2b801d = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.145210028
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3246.61865, 129.480164, 1165.79553, 1
                }
                name: string = "Light_DarkBlue23"
            }
            0x79ce58a9 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.176853582
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2742.97827, 150.915924, 3103.04907, 1
                }
                name: string = "Light_DarkBlue24"
            }
            0xfd332e02 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.123471409
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1532.50171, 90.6044998, 3103.04907, 1
                }
                name: string = "Light_DarkBlue25"
            }
            0x44936755 = MapPointLight {
                type: link = 0x925f06fe
                radiusScale: f32 = 0.977619529
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1558.30127, 612.253052, 1607.49854, 1
                }
                name: string = "light_38_3"
            }
            0x3fc92621 = MapPointLight {
                type: link = 0x925f06fe
                radiusScale: f32 = 0.977619529
                intensityScale: f32 = 1.20000005
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2430.11621, 612.253052, 1607.49854, 1
                }
                name: string = "light_38_4"
            }
            0x051c1e38 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.107087307
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    861.257324, 70.8258438, 897.858398, 1
                }
                name: string = "Light_DarkBlue26"
            }
            0x684eb26f = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.239253372
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2123.03735, 178.336929, 3297.64966, 1
                }
                name: string = "Light_DarkBlue27"
            }
            0x0f0ca4a0 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.157545894
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    782.910583, 158.841827, 3120.95337, 1
                }
                name: string = "Light_DarkBlue28"
            }
            0xead945f2 = MapPointLight {
                type: link = 0xf402c51c
                radiusScale: f32 = 0.300000012
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1836.81592, 275.691681, 3291.64282, 1
                }
                name: string = "Light_White1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Lighting_WintersClaw"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Audio_WintersClaw" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xbecee258 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1029.12903, 338.348999, 930.099976, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Fire1"
            }
            0x1fd654f8 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2977.2334, 338.348999, 932.335083, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Fire2"
            }
            0xf33fe838 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2977.12598, 338.348999, 3028.96509, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Fire3"
            }
            0x1e9c9d6d = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Fire"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1029.12903, 338.348999, 3025.29419, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Fire4"
            }
            0xfc6e3bab = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Air_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2011.32397, -0.00048828125, 2179.12573, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Air_Loop1"
            }
            0xd6c07866 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Lantern_Squeaks_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3790.59863, 278.249878, 1966.31274, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Lantern_Squeaks_Loop1"
            }
            0x4e55d8ce = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Cloth_Flaps_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    703.247803, -515.47876, 1916.26343, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Cloth_Flaps_Loop1"
            }
            0xa13debf8 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Cast"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    4719.09277, 0, 1950.7522, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Cast1"
            }
            0x3cea1035 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Cast"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    22.5970459, -884.742676, 2418.62549, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Cast2"
            }
            0x2f2c0590 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3564.63989, 0, 1620.08679, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Loop1"
            }
            0x18283058 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    539.30249, 394.303589, 1948.16479, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Heavywinds_Loop2"
            }
            0x21dcfe33 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Structure_Crumble_Distant"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    417.509521, 0, 2302.78467, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Structure_Crumble_Distant1"
            }
            0xfb697e2c = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Audio-Emitter_Freljord_WintersClaw_Structure_Crumble_Distant"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3949.67773, -300.569824, 2496.06396, 1
                }
                name: string = "TFT_Audio-Emitter_Freljord_WintersClaw_Structure_Crumble_Distant2"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Audio_WintersClaw"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Art_Shared" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x96cf3b17 = null
            0x8cdb744d = null
            0x185af8f1 = null
            0x7f04abf5 = null
            0xc53ce72c = null
            0x60f8df0b = MapGroup {
                members: list2[string] = {
                    "fa81f9f7-dae1-4efa-8fa4-38d81590378d"
                    "a727a693-7957-41e0-9445-c0c2a859738f"
                }
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    3624.02661, -289.353882, 2712.75415, 1
                }
                name: string = "group1"
            }
            0x7c3a08ff = null
            0x017b3118 = null
            0x0f77f79e = MapGroup {
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    3897.4104, -1233.99731, 951.408203, 1
                }
                name: string = "group2"
            }
            0xd3c64d4c = null
            0x0c0c4621 = null
            0xc0a9295a = null
            0x842b30ce = null
            0x6dd2d5ea = null
            0x88f203dc = null
            0x6f594ec9 = null
            0xae96d0ba = null
            0x4b00daf5 = null
            0xb94027d1 = null
            0xecf2c869 = null
            0x1d1ca7fc = null
            0xd57b11a4 = null
            0xcbdbdbed = null
            0xd5dafdf1 = null
            0x06b3b399 = null
            0x0b05ad8d = null
            0x7b263331 = null
            0xb06f0919 = null
            0xb3ce48e0 = null
            0xa1e92f32 = null
            0xef28381a = null
            0x1677a040 = null
            0x62f75261 = null
            0xa3b715aa = null
            0x05448ec3 = null
            0xfda50dde = null
            0xdfe0551b = null
            0x9e7579da = null
            0xf6c9a647 = null
            0x3886890b = null
            0x7d3cdada = null
            0xee53c70a = null
            0x0d6c99f8 = null
            0x87c296bf = null
            0x1e87857e = null
            0x59b0217c = null
            0x2339622f = null
            0x042ec4ec = null
            0x2a6ecf92 = null
            0x11328b65 = null
            0xf6807de9 = null
            0xc7d71864 = null
            0xe95fafab = null
            0xf41cf36c = null
            0x57074043 = null
            0x5b5c1b1b = null
            0x2b655c22 = null
            0x64018cd4 = null
            0x61781b13 = null
            0x6198f647 = null
            0x31072a88 = null
            0x57321d2c = null
            0x0ac817ff = null
            0xba658b19 = null
            0xb0c9543d = null
            0x07c1b209 = null
            0x45aeaa4e = null
            0xb65ea301 = null
            0xcc7a56c5 = null
            0xcbdbc144 = null
            0x99acfc11 = null
            0xd1f683d5 = null
            0x300f1bb5 = null
            0x810f6bd2 = null
            0x88e05c9c = null
            0x466550f6 = null
            0xf7d7c608 = null
            0x3e9a0284 = null
            0x5f3d89f0 = null
            0x9e425297 = null
            0x7721da20 = null
            0x24b3a5af = null
            0x75b41dae = null
            0x6c17daec = null
            0x60f9bb2c = null
            0x39095c6f = null
            0x5a144719 = null
            0xd40caae1 = null
            0x783c1b36 = null
            0x2d79630b = null
            0x9257b4ed = null
            0xaaddf029 = null
            0xa0a8a3c3 = null
            0xe46fb61e = null
            0x41126533 = null
            0xa282ee9c = null
            0x43d01893 = null
            0x15240e4d = null
            0x5156372a = null
            0xd59bb555 = null
            0xe085e0cc = null
            0x532ab14e = null
            0xe1b4e328 = null
            0x93e26cee = null
            0xb9763556 = null
            0x63d1ca73 = null
            0x07f2951e = null
            0xe2074798 = null
            0xb5a8eb20 = null
            0xe33a3d85 = null
            0x7c79c110 = null
            0xf54ab6bc = null
            0x7611930f = null
            0x2b388211 = null
            0x8d6edcab = null
            0xc25581de = null
            0xb424065f = null
            0xfd117cfe = null
            0xd6e24041 = null
            0xf86f6bb5 = null
            0x0e2df091 = null
            0x5a70ff2c = null
            0x6bac4e6b = null
            0x49dd0f8c = null
            0x9adf1ecf = null
            0x7c6f44d6 = null
            0x7a234714 = null
            0xf839a9f9 = null
            0x316bbd34 = null
            0xf25d3250 = null
            0x0633f04a = null
            0x48c425f2 = null
            0x02e881dc = null
            0x99dafaac = null
            0xf5fcd608 = null
            0xe2acdeb1 = null
            0xd39f9ecc = null
            0x6dc740d2 = null
            0xc6f18fec = null
            0x87b8f3e2 = null
            0x1de0447d = null
            0x38c6c0ae = null
            0xc6145035 = null
            0xf500d365 = null
            0xecc2445d = null
            0xd0f89eed = null
            0x06d51709 = null
            0xd7c23dbd = null
            0x39dbef9e = null
            0x2cf5a52c = null
            0x57515a47 = null
            0x22d12f9f = null
            0x34e0ebc3 = null
            0x16372994 = null
            0x5bb0f73a = null
            0x1fcd9b0d = null
            0xd96126f4 = null
            0x781cfce6 = null
            0x1cab8909 = null
            0x59a8caf6 = null
            0x17e6b6c2 = null
            0xdbe38656 = null
            0xee4d3496 = null
            0x5347c307 = null
            0x9ee2888c = null
            0x17a1a151 = null
            0xb6beb28a = null
            0x74e7405a = null
            0xaef471f0 = null
            0x72e59f67 = null
            0x94951a84 = null
            0xc930ee6c = null
            0x7bd6890d = null
            0xbb42673e = null
            0xa1c6020e = null
            0x87edee67 = null
            0xc912d7cd = null
            0x43f55e27 = null
            0x826ca080 = null
            0xb30ea4a2 = null
            0x44a4ffac = null
            0x140ef17d = null
            0x9c5f2c26 = null
            0x48c9c0d7 = null
            0xe07bf76c = null
            0x68aebc46 = null
            0x66616f4b = null
            0x519a86c6 = null
            0x954c617a = null
            0xc5eef00e = null
            0xf8177c41 = null
            0xdbdcf0b4 = null
            0x2c908866 = null
            0x0a45175a = null
            0x25624a73 = null
            0x8d76ba2c = null
            0xca2f0847 = null
            0xfff796d5 = null
            0x399f1c45 = null
            0x5e2bd6f8 = null
            0x93d079c5 = null
            0xc24a9782 = null
            0x90d8d142 = null
            0x3285f24c = null
            0x13160753 = null
            0x66b0378b = null
            0x26ebe58a = null
            0xb58c225c = null
            0xcaddbe9f = null
            0x07ec5489 = null
            0xf4077d0b = null
            0x58ada8cf = null
            0x1c055875 = null
            0x80aab86e = null
            0xfc0ffc7a = null
            0x5888fc52 = null
            0x0d584327 = null
            0x791463b6 = null
            0xf2bf8e13 = null
            0xc23412ff = null
            0xd2430d2a = null
            0x551d1e9e = null
            0xf2724f8d = null
            0x0afa0573 = null
            0xb51be10c = null
            0xf7742e34 = null
            0x98249bf2 = null
            0x62626809 = null
            0x162e59c2 = null
            0x87d1939a = MapGroup {
                members: list2[string] = {
                    "24f70617-3890-4d47-a7c5-dd13f102bcd8"
                    "73744f69-e6b6-4c59-9899-170fa3b58a1e"
                }
                transform: mtx44 = {
                    -0.999999523, 0, 2.38418551e-07, 0
                    0, 1, 0, 0
                    -2.38418551e-07, 0, -0.999999523, 0
                    1009.45764, 136.666626, 2720.69995, 1
                }
                name: string = "group3"
            }
            0xac821b5e = null
            0xc9c71e54 = null
            0xc4b4250b = null
            0x401ddfa1 = null
            0x2796299c = null
            0x42911f36 = null
            0x3d17ef87 = null
            0xf9db0e40 = null
            0xdc7b58b0 = null
            0x81e54b8d = null
            0x41934d92 = null
            0x36b07081 = null
            0x8eb4917e = null
            0x1ffca1fd = null
            0x2bf2365f = null
            0xcdde7826 = null
            0x29e82a87 = null
            0x796d2707 = null
            0x145aae8c = null
            0xc190a344 = null
            0xac453af7 = null
            0xc23ee4e7 = null
            0x40e512fe = null
            0x9ebc624f = null
            0x6e66ebb6 = null
            0x9400b9b7 = null
            0x9f5e3c98 = null
            0x0d4f2db1 = null
            0x4790794f = null
            0x43f48220 = null
            0x0bc4ed1e = null
            0xe70f9a1a = null
            0x9213a4f5 = null
            0x099bd012 = null
            0xe9f1533e = null
            0x58d4474d = null
            0x29f528b0 = null
            0x0f4731cb = null
            0x29eea516 = null
            0xb7971511 = null
            0x03c3e6db = null
            0xef8b63b2 = null
            0x150036c7 = null
            0x6a40ce98 = null
            0x5b18b966 = null
            0x173a65a5 = null
            0xe6e57258 = null
            0x3385d815 = null
            0xf18e1d85 = null
            0x16848946 = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Art_Shared"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/LevelProps_Shared" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x53c15a9e = GdsMapObject {
                type: u8 = 10
                boxMin: vec3 = { 950.559814, 185.223526, 2651.823 }
                boxMax: vec3 = { 1021.02734, 234.593903, 2722.29077 }
                extraInfo: list[pointer] = {
                    GDSMapObjectAnimationInfo {
                        defaultAnimation: string = "idle1"
                    }
                }
                0xad304db5: string = "Characters/HA_AP_Poro/Skins/Skin0"
                sceneLayer: string = "Level Props"
                transform: mtx44 = {
                    -0.274249792, 0, -0.961658657, 0
                    0, 1, 0, 0
                    0.961658657, 0, -0.274249792, 0
                    985.793579, 184.135818, 2687.05688, 1
                }
                name: string = "LevelProp_TFT_BoardPoro"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/LevelProps_Shared"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/VFX_WintersClaw" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x779f86e6 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Godrays"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000.6051, -129.80484, 1928.62354, 1
                }
                name: string = "TFT_Freljord_Godrays2"
            }
            0xeb49e3b2 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Snow"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    33.9648438, 69.9951706, 1930.54834, 1
                }
                name: string = "TFT_Freljord_Snow3"
            }
            0x652d3023 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Godrays"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000.6051, -129.80484, 1928.62354, 1
                }
                name: string = "TFT_Freljord_Godrays3"
            }
            0xe9afb35e = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1996.22754, 258.248535, 898.782349, 1
                }
                name: string = "TFT_Freljord_Wind3"
            }
            0x7a81b689 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_WintersClaw"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1030.49695, 260, 931.027771, 1
                }
                name: string = "TFT_BrazierFire_C1"
            }
            0x458244c8 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_WintersClaw"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2978.66602, 260, 929.722595, 1
                }
                name: string = "TFT_BrazierFire_C2"
            }
            0x195d9bb7 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_WintersClaw"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1026.276, 260, 3022.49316, 1
                }
                name: string = "TFT_BrazierFire_C3"
            }
            0xb06d6575 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_WintersClaw"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2978.18384, 260, 3025.9707, 1
                }
                name: string = "TFT_BrazierFire_C4"
            }
            0x7320a307 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1983.06763, 239.668457, 250.650391, 1
                }
                name: string = "TFT_Freljord_WintersClaw_Fog2"
            }
            0x6d1bd0d2 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1976.46387, -147.717041, 232.359497, 1
                }
                name: string = "TFT_Freljord_WintersClaw_Fog1"
            }
            0xcae4f7af = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1996.22754, 129.836792, 3230.57886, 1
                }
                name: string = "TFT_Freljord_Wind1"
            }
            0x6cabb58f = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Flurries"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2936.20679, 92.6318359, 1032.10767, 1
                }
                name: string = "TFT_Freljord_WintersClaw_Flurries1"
            }
            0xbcb08bcc = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Flurries"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3042.13696, 192.563416, 3118.80469, 1
                }
                name: string = "TFT_Freljord_WintersClaw_Flurries3"
            }
            0x5c7b66eb = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Flurries"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    969.873291, 24.3696289, 3036.08789, 1
                }
                name: string = "TFT_Freljord_WintersClaw_Flurries4"
            }
            0x9fef83ea = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Edge_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2011.19763, 173.938416, 866.54187, 1
                }
                name: string = "TFT_Freljord_WintersClaw_Edge_Fog1"
            }
            0x9449178a = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Edge_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2011.19763, 131.327209, 3264.604, 1
                }
                name: string = "TFT_Freljord_WintersClaw_Edge_Fog2"
            }
            0x38df8dad = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Edge_Fog"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    849.733032, -219.4151, 1938.61841, 1
                }
                name: string = "TFT_Freljord_WintersClaw_Edge_Fog3"
            }
            0xe6328790 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Flurries"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    946.017822, 70.7160645, 1233.93896, 1
                }
                name: string = "TFT_Freljord_WintersClaw_Flurries5"
            }
            0x936b9f3d = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_WintersClaw_Edge_Flurries"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    954.440918, 46.5192871, 1982.00366, 1
                }
                name: string = "TFT_Freljord_WintersClaw_Edge_Flurries1"
            }
            0xced1f474 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_WintersClaw"
                transform: mtx44 = {
                    0.649999976, 0, 0, 0
                    0, 0.649999976, 0, 0
                    0, 0, 0.649999976, 0
                    3682.31128, -398.208649, 2176.18286, 1
                }
                name: string = "TFT_BrazierFire_C5"
            }
            0xdc9f3442 = MapParticle {
                system: link = "Maps/Particles/TFT/Freljord/TFT_Freljord_BrazierFire_WintersClaw"
                transform: mtx44 = {
                    0.649999976, 0, 0, 0
                    0, 0.649999976, 0, 0
                    0, 0, 0.649999976, 0
                    412.575806, -398.208649, 2174.91894, 1
                }
                name: string = "TFT_BrazierFire_C6"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/VFX_WintersClaw"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Art_WintersClaw" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x6718756b = null
            0xf6da8d3f = null
            0x5f8871e2 = null
            0xd6be26b5 = null
            0x07d5fec8 = null
            0x2149b6f3 = null
            0xb6fa99a6 = null
            0x4b7d158e = null
            0x2b9ced18 = null
            0xaed16ab5 = null
            0xf7ec58e3 = null
            0xc7f5649b = null
            0x384a9798 = null
            0x6e8d8ff2 = null
            0x4416571a = null
            0x87b9fb37 = null
            0x85fd68e0 = null
            0x874b7244 = null
            0x588599e3 = null
            0xdcdd74d0 = null
            0x8738cd34 = null
            0xd432935b = null
            0x2beb71d2 = null
            0x20f0fe04 = null
            0xcf54c0c4 = null
            0xe2a62c37 = null
            0x5d154732 = null
            0x7b91ba70 = null
            0x6ff563b2 = null
            0xcd6d9495 = null
            0x189ff94d = null
            0xe1a2167c = null
            0x48b09f79 = null
            0x0a3ce11e = null
            0x504deb85 = null
            0xe13277ec = null
            0x7e92b1a8 = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Art_WintersClaw"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/LightingVolume_WintersClaw" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xa00ad13a = MapLightingVolume {
                sunColor: vec4 = { 0.223529413, 0.333333343, 0.368627459, 0.972549021 }
                sunDirection: vec3 = { 0.150000006, 0.827000022, 0.150000006 }
                0xd8851203: f32 = 15
                skyLightColor: vec4 = { 0.145098045, 0.196078435, 0.290196091, 1 }
                horizonColor: vec4 = { 0.65882355, 0.886274517, 0.905882359, 1 }
                groundColor: vec4 = { 0.56078434, 0.458823532, 0.321568638, 1 }
                skyLightScale: f32 = 0.75
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.513725519, 0.596078455, 0.615686297, 1 }
                fogAlternateColor: vec4 = { 0.0980392173, 0.141176477, 0.23137255, 1 }
                fogStartAndEnd: vec2 = { 700, -2000 }
                transform: mtx44 = {
                    2850.56348, 0, 0, 0
                    0, 4337.81396, 0, 0
                    0, 0, 3098.43872, 0
                    2032.48315, -1416.61292, 2193.8706, 1
                }
                name: string = "LightingVolume1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/LightingVolume_WintersClaw"
    }
    "Maps/MapGeometry/Map22/Chunks/Freljord/Skybox_Freljord" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xdf91013f = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Freljord/Skybox_Freljord"
    }
    "Maps/MapGeometry/Map22/Chunks/Base/Freljord_Design_Base" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xf7e857de = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Spawn_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2912.56494, 3, 2291.08301, 1
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
                    1110.23596, 0, 1693.47803, 1
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
                    2791.72803, 0, 2892.43091, 1
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
                    3050.87988, 0, 2846.68994, 1
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
                    928.268982, 0, 1132.08398, 1
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
                    -0.99999994, 8.74227766e-08, 0, 0
                    8.74227695e-08, 0.999999881, 8.74227766e-08, 0
                    7.64274186e-15, 8.74227695e-08, -0.99999994, 0
                    2067, 0, 2394, 1
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
                    1142.53601, 0, 1411.255, 1
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
                    2863.53394, 0, 2627.49097, 1
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
        path: string = "Maps/MapGeometry/Map22/Chunks/Base/Freljord_Design_Base"
    }
    "Maps/MapGeometry/Map22/Freljord_WintersClaw" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/Freljord_WintersClaw"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.643137276, 0.650980413, 0.572549045, 1 }
                sunDirection: vec3 = { -0.384805739, 0.827142715, -0.409584463 }
                0xd8851203: f32 = 75
                skyLightColor: vec4 = { 0.431372553, 0.498039216, 0.474509805, 1 }
                horizonColor: vec4 = { 0.301960796, 0.368627459, 0.509803951, 1 }
                groundColor: vec4 = { 0.250980407, 0.215686277, 0.392156869, 1 }
                skyLightScale: f32 = 0.300000012
                lightMapColorScale: f32 = 2.5
                fogEnabled: bool = false
                fogColor: vec4 = { 0.423529416, 0.752941191, 0.870588243, 1 }
                fogAlternateColor: vec4 = { 0.305882365, 0.392156869, 0.68235296, 1 }
                fogStartAndEnd: vec2 = { -1000, -20000 }
                fogEmissiveRemap: f32 = 1
                useBloom: bool = true
            }
            MapBakeProperties {
                0x22d24a9a: f32 = 1.5
                lightGridCharacterFullBrightIntensity: f32 = 0.5
                0x2f3b5471: f32 = 2
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/Freljord_WintersClaw/LightGrid.TFT_1023_LightingUpdate.dat"
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.800000012
            }
            MapNavGrid {
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/WintersClaw_Navgrid.aimesh_ngrid"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            0xfff6d589 = "Maps/MapGeometry/Map22/Chunks/Freljord/Art_Shared"
            0xae22a63c = "Maps/MapGeometry/Map22/Chunks/Freljord/VFX_WintersClaw"
            0x3bb78eb4 = "Maps/MapGeometry/Map22/Chunks/Freljord/Lighting_WintersClaw"
            0x8735d352 = "Maps/MapGeometry/Map22/Chunks/Freljord/LightingVolume_WintersClaw"
            0x858398a9 = "Maps/MapGeometry/Map22/Chunks/Freljord/Art_WintersClaw"
            0x1f286b3a = "Maps/MapGeometry/Map22/Chunks/Freljord/Audio_WintersClaw"
            "Skybox_Freljord" = "Maps/MapGeometry/Map22/Chunks/Freljord/Skybox_Freljord"
            "LevelProps_Shared" = "Maps/MapGeometry/Map22/Chunks/Freljord/LevelProps_Shared"
            "Freljord_Design_Base" = "Maps/MapGeometry/Map22/Chunks/Base/Freljord_Design_Base"
        }
    }
    0x7ca5e4f1 = MapPointLightType {
        lightColor: vec4 = { 0.105882354, 0.321568638, 0.713725507, 1 }
        radius: f32 = 1096
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0x925f06fe = MapPointLightType {
        lightColor: vec4 = { 0.564705908, 0.490196079, 0.713725507, 1 }
        radius: f32 = 1096
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0xe25bb04b = MapPointLightType {
        lightColor: vec4 = { 0.301960796, 0.607843161, 0.694117665, 1 }
        radius: f32 = 1051
        castStaticShadows: bool = false
    }
    0xf402c51c = MapPointLightType {
        lightColor: vec4 = { 0.854902029, 0.854902029, 0.992156923, 1 }
        radius: f32 = 1140
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0xf449b3ec = MapPointLightType {
        lightColor: vec4 = { 0.988235295, 0.266666681, 0, 1 }
        radius: f32 = 719
        castStaticShadows: bool = false
    }
}
