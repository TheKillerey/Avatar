#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    0x3941e075 = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Set5/Materials/Default/Harmony_Skybox_A_MAT"
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
    0x49627140 = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Set5/Materials/Default/Harmony_Skybox_B_MAT"
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
                        shaderMacros: map[string,string] = {
                            "NO_BAKED_LIGHTING" = "1"
                            "DISABLE_DEPTH_FOG" = "1"
                        }
                    }
                }
            }
        }
    }
    0x4d2a4dfa = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Set5/Materials/Default/Harmony_StatueBase_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Set5/Textures/Harmony_StatueBase_A.TFT_ArenaSkin_Set5.dds"
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
    0x4f989f17 = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Set5/Materials/Default/Order_Cliff_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Set5/Textures/Order_Cliff_A.TFT_ArenaSkin_Set5.dds"
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
    0x55d4a9f5 = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Set5/Materials/Default/Harmony_Ivy_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Set5/Textures/Harmony_Ivy_A.TFT_ArenaSkin_Set5.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "AlphaTestValue"
                value: vec4 = { 0.75, 0, 0, 0 }
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
    0x7219304f = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Set5/Materials/Default/Harmony_Root_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Set5/Textures/Harmony_Root_A.TFT_ArenaSkin_Set5.dds"
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
    0x75f6b853 = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Set5/Materials/Default/Board_Harmony_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Set5/Textures/Board_Harmony.TFT_ArenaSkin_Set5.dds"
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
    0xb393810d = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Set5/Materials/Default/Harmony_CultureKit_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Set5/Textures/Harmony_CultureKit_A.TFT_ArenaSkin_Set5.dds"
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
    0xb96b2852 = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Set5/Materials/Default/Harmony_Anatomy_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Set5/Textures/Harmony_Anatomy_A.TFT_ArenaSkin_Set5.dds"
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
    0xfc7ebd4a = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Set5/Materials/Default/Harmony_Brazier_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Set5/Textures/Harmony_Brazier_A.TFT_ArenaSkin_Set5.dds"
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
    "Maps/Particles/TFT/Base/TFT_BrazierFire_A" = VfxSystemDefinitionData {
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
                pass: i16 = 2
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
                pass: i16 = -2
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
        particlePath: string = "Maps/Particles/TFT/Base/TFT_BrazierFire_A"
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
    0x1044fefe = MapPlaceableContainer {
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
        path: string = "Maps/MapGeometry/Map22/Chunks/Set5/Set5_Design_Base_3"
    }
    0x1c50d8ad = MapPlaceableContainer {
        path: string = "Maps/MapGeometry/Map22/Chunks/Set5/Periph_Harmony"
    }
    0x26d93709 = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x729cd81f = MapLightingVolume {
                sunColor: vec4 = { 0.615686297, 0.580392182, 0.556862772, 1 }
                sunDirection: vec3 = { 0.25, 0.52700001, -0.200000003 }
                0xd8851203: f32 = 75
                0xba02f116: f32 = 0.150000006
                skyLightColor: vec4 = { 0.615686297, 0.580392182, 0.556862772, 1 }
                horizonColor: vec4 = { 0.541176498, 0.549019635, 0.450980395, 1 }
                groundColor: vec4 = { 0.458823532, 0.521568656, 0.556862772, 1 }
                skyLightScale: f32 = 0.550000012
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.188235298, 0.211764708, 0.388235301, 1 }
                fogAlternateColor: vec4 = { 0.290196091, 0.20784314, 0.117647059, 1 }
                fogStartAndEnd: vec2 = { 500, -1100 }
                transform: mtx44 = {
                    2795.28564, 0, 0, 0
                    0, 5183.96924, 0, 0
                    0, 0, 3295.46655, 0
                    2000, 0, 2000, 1
                }
                name: string = "LightingVolume1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Set5/LightingVolume_Harmony"
    }
    0x3255ffa2 = MapPlaceableContainer {
        path: string = "Maps/MapGeometry/Map22/Chunks/Set5/AnimProps_Harmony"
    }
    0x520a2eaf = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xa8957e38 = MapPointLight {
                type: link = 0x4112ec52
                radiusScale: f32 = 0.93599993
                intensityScale: f32 = 0.200000003
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2833.91187, 327.441711, 2605.67529, 1
                }
                name: string = "SoftYellow_Point1"
            }
            0x82e68246 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2006.21106, 416.604584, 1133.2456, 1
                }
                name: string = "SoftWhite_Point2"
            }
            0xb1e84b40 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2552.21436, 416.604584, 1133.2456, 1
                }
                name: string = "SoftWhite_Point3"
            }
            0x22e3b436 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 0.93599993
                intensityScale: f32 = 0.200000003
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2833.91211, 343.324707, 2605.67505, 1
                }
                name: string = "SoftWhite_Point4"
            }
            0xc7686841 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1409.87634, 416.604584, 2904.54419, 1
                }
                name: string = "SoftWhite_Point5"
            }
            0xfa7b850a = MapPointLight {
                type: link = 0x4112ec52
                radiusScale: f32 = 0.935731053
                intensityScale: f32 = 0.400000006
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1253.58081, 327.441711, 1392.80774, 1
                }
                name: string = "SoftYellow_Point2"
            }
            0xabbffd70 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2596.58545, 416.604584, 2904.54419, 1
                }
                name: string = "SoftWhite_Point6"
            }
            0x3102b12b = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 0.93599993
                intensityScale: f32 = 0.400000006
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1253.58105, 359.195892, 1392.80798, 1
                }
                name: string = "SoftWhite_Point7"
            }
            0x0cef3847 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2006.21106, 416.604584, 2904.54419, 1
                }
                name: string = "SoftWhite_Point9"
            }
            0x34854b73 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 1.20000005
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1461.05469, 416.604584, 1133.2456, 1
                }
                name: string = "SoftWhite_Point10"
            }
            0xf4d5f4c8 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 2.94112921
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2006.21106, 746.768127, 2038.93909, 1
                }
                name: string = "SoftWhite_Point11"
            }
            0xdfe616e8 = MapPointLight {
                type: link = 0xe81e6598
                radiusScale: f32 = 0.424999982
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1068.68555, 234.659332, 997.802124, 1
                }
                name: string = "SoftOrange_Point_Club2_1"
            }
            0x47d9643c = MapPointLight {
                type: link = 0x9e87f2f2
                radiusScale: f32 = 0.744999945
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1068.68579, 253.958145, 997.802002, 1
                }
                name: string = "Red_Point_Set5_1"
            }
            0x0d094082 = MapPointLight {
                type: link = 0x9e87f2f2
                radiusScale: f32 = 0.745000005
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2884.81763, 253.958145, 997.802002, 1
                }
                name: string = "Red_Point_Set5_2"
            }
            0xe8a02880 = MapPointLight {
                type: link = 0xe81e6598
                radiusScale: f32 = 0.425000012
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2884.81763, 234.659332, 997.802124, 1
                }
                name: string = "SoftOrange_Point_Club2_2"
            }
            0x89dee690 = MapPointLight {
                type: link = 0x9e87f2f2
                radiusScale: f32 = 0.744999945
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2929.00903, 253.958145, 3058.03808, 1
                }
                name: string = "Red_Point_Set5_3"
            }
            0x8b4be5c9 = MapPointLight {
                type: link = 0xe81e6598
                radiusScale: f32 = 0.424999982
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2929.00903, 234.659332, 3058.03833, 1
                }
                name: string = "SoftOrange_Point_Club2_3"
            }
            0x6ee4e02a = MapPointLight {
                type: link = 0x9e87f2f2
                radiusScale: f32 = 0.745000005
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1119.68799, 253.958145, 3058.03808, 1
                }
                name: string = "Red_Point_Set5_4"
            }
            0x27fea5f3 = MapPointLight {
                type: link = 0xe81e6598
                radiusScale: f32 = 0.425000012
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1119.68799, 234.659332, 3058.03833, 1
                }
                name: string = "SoftOrange_Point_Club2_4"
            }
            0xf9b21abb = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 0.600000024
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3110.20947, 796.978149, 1582.63062, 1
                }
                name: string = "SoftWhite_Point1"
            }
            0x6da15555 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 0.600000024
                intensityScale: f32 = 0.899999976
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1888.66736, 188.908173, 889.938476, 1
                }
                name: string = "SoftWhite_Point8"
            }
            0x76ce5ea2 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 0.600000024
                intensityScale: f32 = 0.699999988
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1470.07214, 136.063553, 889.938476, 1
                }
                name: string = "SoftWhite_Point12"
            }
            0x21321933 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 0.899999976
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    891.659058, 796.978149, 2522.56152, 1
                }
                name: string = "SoftWhite_Point13"
            }
            0xc160734d = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 0.600000024
                intensityScale: f32 = 0.600000024
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    894.648193, 796.978149, 987.764893, 1
                }
                name: string = "SoftWhite_Point14"
            }
            0xf3304b69 = MapPointLight {
                type: link = 0xbea7d96e
                radiusScale: f32 = 0.600000024
                intensityScale: f32 = 0.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3108.91187, 761.650269, 3068.35815, 1
                }
                name: string = "SoftWhite_Point15"
            }
            0xf577af73 = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                intensity: f32 = 1.75
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_B.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.448096216, -0.0898197591, -0.889461696, 0
                    -0.786178708, 0.513249815, 0.344234884, 0
                    0.425596893, 0.853526235, -0.300599724, 0
                    3216.2644, 976.279907, 1285.66003, 1
                }
                name: string = "GenericSpotLight1"
            }
            0xd5e88876 = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                intensity: f32 = 1.25
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_C.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.448012292, -0.0898745656, -0.889498413, 0
                    -0.78622663, 0.513240218, 0.344139934, 0
                    0.425596833, 0.853526235, -0.300599724, 0
                    2681.91894, 976.279907, 2070.76514, 1
                }
                name: string = "GenericSpotLight2"
            }
            0x0a17fd5a = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                intensity: f32 = 1.25
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_D.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.0196936019, -0.323371351, -0.946067154, 0
                    -0.904698551, 0.408563197, -0.120816886, 0
                    0.425596893, 0.853526235, -0.300599724, 0
                    1475.64563, 1309.81653, 1919.29321, 1
                }
                name: string = "GenericSpotLight3"
            }
            0x1048a35b = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                intensity: f32 = 2
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_E.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.418559998, -0.108837917, -0.901643932, 0
                    -0.802293479, 0.509555936, 0.310930848, 0
                    0.425596833, 0.853526235, -0.300599694, 0
                    2066.43506, 1044.42993, 2462.66577, 1
                }
                name: string = "GenericSpotLight4"
            }
            0x84e78d55 = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                intensity: f32 = 2
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_E.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.0196936019, -0.323371351, -0.946067154, 0
                    -0.904698551, 0.408563197, -0.120816886, 0
                    0.425596893, 0.853526235, -0.300599724, 0
                    2528.33936, 951.658936, 694.092468, 1
                }
                name: string = "GenericSpotLight5"
            }
            0xf967f83f = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                intensity: f32 = 1.25
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_C.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.5166623, -0.043522507, -0.855082333, 0
                    -0.742918134, 0.519228995, 0.422461808, 0
                    0.425596893, 0.853526235, -0.300599754, 0
                    1605.81384, 1037.37476, 1107.12048, 1
                }
                name: string = "GenericSpotLight6"
            }
            0x628ffd3b = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                intensity: f32 = 2
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_C.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.351331294, -0.150273547, -0.924112558, 0
                    -0.833926618, 0.498909622, 0.235914528, 0
                    0.425596863, 0.853526235, -0.300599754, 0
                    3488.3374, 1076.88196, 2408.64282, 1
                }
                name: string = "GenericSpotLight8"
            }
            0x106c64b4 = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_D.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.0196936019, -0.323371351, -0.946067154, 0
                    -0.904698551, 0.408563197, -0.120816886, 0
                    0.425596893, 0.853526235, -0.300599724, 0
                    2423.9104, 1172.92456, 1496.1582, 1
                }
                name: string = "GenericSpotLight9"
            }
            0x7f2c61e9 = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                intensity: f32 = 3.5
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_B.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.389393747, -0.127119035, -0.912257195, 0
                    -0.816847503, 0.505305529, 0.278256297, 0
                    0.425596863, 0.853526175, -0.300599724, 0
                    3614.31934, 787.446106, 785.054688, 1
                }
                name: string = "GenericSpotLight7"
            }
            0xf5f42ac8 = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                intensity: f32 = 3.5
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_B.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.0196936019, -0.323371351, -0.946067154, 0
                    -0.904698551, 0.408563197, -0.120816886, 0
                    0.425596893, 0.853526235, -0.300599724, 0
                    1257.18018, 857.156921, 398.33313, 1
                }
                name: string = "GenericSpotLight10"
            }
            0xb45cea98 = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                intensity: f32 = 4
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_D.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.0196936019, -0.323371351, -0.946067154, 0
                    -0.904698551, 0.408563197, -0.120816886, 0
                    0.425596893, 0.853526235, -0.300599724, 0
                    1373.87512, 1030.02563, 2568.56567, 1
                }
                name: string = "GenericSpotLight11"
            }
            0x825876b3 = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                intensity: f32 = 1.75
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_B.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.683591366, 0.0855872259, -0.724829316, 0
                    -0.592933357, 0.51397258, 0.619888902, 0
                    0.425596863, 0.853526175, -0.300599724, 0
                    1365.3479, 976.279907, 1751.38696, 1
                }
                name: string = "GenericSpotLight12"
            }
            0x7fda5883 = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                intensity: f32 = 1.75
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_B.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.547535539, -0.0215849839, -0.836503983, 0
                    -0.720466554, 0.520602584, 0.458149463, 0
                    0.425596893, 0.853526175, -0.300599724, 0
                    1229.21753, 976.279907, 1062.28662, 1
                }
                name: string = "GenericSpotLight13"
            }
            0x7b6f5395 = 0xd11fafa3 {
                color: vec4 = { 1, 0.819607854, 0.596078455, 1 }
                intensity: f32 = 2
                Impact: i32 = 1
                0x99e6dbfe: string = "ASSETS/Maps/SpotLights/LightMask_Canopy_B.png"
                falloffTexture: string = "ASSETS/Maps/SpotLights/linear_2.png"
                far: f32 = 1750
                0xb0f389dc: f32 = 40
                transform: mtx44 = {
                    -0.683591366, 0.0855872259, -0.724829316, 0
                    -0.592933357, 0.51397258, 0.619888902, 0
                    0.425596863, 0.853526175, -0.300599724, 0
                    3541.87109, 871.83606, 1183.15894, 1
                }
                name: string = "GenericSpotLight14"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Set5/Lighting_Harmony"
    }
    0x9b7502fa = MapPlaceableContainer {
        path: string = "Maps/MapGeometry/Map22/Chunks/Set5/MapBehaviors_Harmony"
    }
    0xa19d69d1 = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xd33bb2dc = MapParticle {
                system: link = "Maps/Particles/TFT/TFT_Skybox"
                transform: mtx44 = {
                    0.99999994, 0, 0, 0
                    0, 0.99999994, 0, 0
                    0, 0, 0.999999881, 0
                    2000, 18.6369991, 2000, 1
                }
                name: string = "TFT_Skybox2"
                0xccf79327: u8 = 126
            }
            0x8241b80f = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Set5/Skybox_Harmony"
    }
    0xaf8ee171 = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x84552a9d = 0xa783cfd5 {
                0x2a078c9c: string = "Play_sfx_tft_env_set5_harmony_amb"
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Camera_Yellow"
                sceneLayer: string = "MapAudio"
                transform: mtx44 = {
                    0.99999994, 0, 0, 0
                    0, 0.99999994, 0, 0
                    0, 0, 0.999999881, 0
                    2000, 0, 2000, 1
                }
                name: string = "MapAudio_Harmony_SFX_Amb"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Set5/Audio_Harmony"
    }
    0xd0d2ba77 = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x24b74d1d = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2882.74341, 151.633423, 987.078003, 1
                }
                name: string = "TFT_BrazierFire_A1"
            }
            0xf2d8a7b4 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2964.29443, 151.633423, 3062.15381, 1
                }
                name: string = "TFT_BrazierFire_A2"
            }
            0xf3a0a221 = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1122.90735, 151.633423, 3062.15381, 1
                }
                name: string = "TFT_BrazierFire_A3"
            }
            0x41246daf = MapParticle {
                system: link = "Maps/Particles/TFT/Base/TFT_BrazierFire_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1035.50305, 151.633423, 987.078003, 1
                }
                name: string = "TFT_BrazierFire_A4"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Set5/VFX_Harmony"
    }
    0xdbc1b627 = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xdcd78a23 = null
            0xe1425d86 = null
            0xce139469 = null
            0xfa624e36 = null
            0x48451f63 = null
            0xd46d2007 = null
            0x9a267829 = null
            0x7c204ac1 = null
            0x229da12d = null
            0x93decddb = null
            0x0a08e9c2 = null
            0x61500bb4 = null
            0x412d9984 = null
            0xd060e2af = null
            0x3955d48e = null
            0xc9d5708e = null
            0xf4bf95b3 = null
            0x85e400e2 = null
            0xf644726f = null
            0x7e23a3ed = null
            0x54730663 = null
            0x65ef71ef = null
            0x951c2f32 = null
            0xa211e564 = null
            0x4d0398c3 = null
            0x28d5d661 = null
            0xc2e0dccb = null
            0x3daecc0c = null
            0x83e03ae7 = null
            0xd9212c3c = null
            0xc553edea = null
            0xd7425fe3 = null
            0xa682d0c7 = null
            0x14276fc4 = null
            0x75e7f6e3 = null
            0xa1dfbfb6 = null
            0x43b7fec5 = null
            0x5ae71d62 = null
            0xaa4022cc = null
            0x685b46b7 = null
            0x87a9c0fd = null
            0x0a61ad8e = null
            0x29f83ee7 = null
            0x4531d78e = null
            0x15b07084 = null
            0x80c26d3e = null
            0x5ccc4a71 = null
            0x84c37f99 = null
            0xff1b63f4 = null
            0xb7d19f7c = null
            0x74090357 = null
            0x2a1aceac = null
            0x89d94fa5 = null
            0x66a4c0d4 = null
            0x09e5e260 = null
            0xe6dd9ced = null
            0x8dc697d7 = null
            0x3e790316 = null
            0x6bffda07 = null
            0xd11e2d27 = null
            0xc8325fea = null
            0x61ea3495 = null
            0xd86db66d = null
            0x200e6486 = null
            0xc9351afb = null
            0x0d1bb510 = null
            0xc5bb7791 = null
            0x29a7707c = null
            0xadcff53a = null
            0x11347502 = null
            0x12ac7abc = null
            0xe786476b = null
            0x3dc8b61c = null
            0x1d8bc67c = null
            0x6e8acb43 = null
            0x1322615a = null
            0x0ae82fdb = null
            0x669f38ab = null
            0x0dc2b7be = null
            0xa4cfb6c6 = null
            0x7fd76f4f = null
            0x5e482b00 = null
            0x2e96e275 = null
            0xcb311139 = null
            0x611b5f73 = null
            0xbaeb4a71 = null
            0x8cc6e722 = null
            0x4c15b388 = null
            0x6f71321d = null
            0xd44d63eb = null
            0x023d6e4c = null
            0x9dc95781 = null
            0xd827f51c = null
            0xe2757a77 = null
            0xfae553ff = null
            0x2169c04c = null
            0x288d9ab3 = null
            0x7516e51e = null
            0x49594a36 = null
            0xd5564ea3 = null
            0x0875c865 = null
            0x550eb948 = null
            0xf93c215c = null
            0xa176a4d2 = null
            0x6d6beb03 = null
            0xd9969084 = null
            0xe05860a7 = null
            0x2134693e = null
            0x65d53379 = null
            0x55c69a09 = null
            0x311b4549 = null
            0x2689d1d3 = null
            0xa6382333 = null
            0x1bca1629 = null
            0x6b0a2f73 = null
            0x53d45b59 = null
            0x17d754ad = null
            0x942ac409 = null
            0xb632b2ec = null
            0x3d6467b3 = null
            0x68295a2c = null
            0x9392accd = null
            0x0840e1e5 = null
            0x4d816a48 = null
            0xe023bcef = null
            0x59b2ad2d = null
            0x082be5f2 = null
            0x30e6040f = null
            0x9a2b0e2b = null
            0x411b07d2 = null
            0xca70b237 = null
            0x64f4ec75 = null
            0x02a2deaa = null
            0x4cf279d6 = null
            0x81c011e9 = null
            0x775129bc = null
            0xcbf2367a = null
            0xe3b299f4 = null
            0xf1b2d2c0 = null
            0x55fb3b6a = null
            0xca33e9ca = null
            0x2cf38331 = null
            0xa64f17fd = null
            0xee58d985 = null
            0xdb1e94f2 = null
            0xebaf582c = null
            0x944bb2ba = null
            0x1bba0b31 = null
            0x17dd26df = null
            0x96114c53 = null
            0x1a49c789 = null
            0x86e7d108 = null
            0xffa9f46d = null
            0xde477411 = null
            0x96fc927b = null
            0xf20d7cd2 = null
            0xba5c5874 = null
            0x87f164ab = null
            0x40a798c5 = null
            0xf8af2447 = null
            0xf623ceb3 = null
            0x55dc0398 = null
            0xf7050384 = null
            0xb1d43237 = null
            0x8ace0df3 = null
            0x69e8ef3f = null
            0xb2301b3a = null
            0x9c1f21a3 = null
            0x41a47c1b = null
            0xa956ce05 = null
            0xb10baf99 = MapGroup {
                members: list2[string] = {
                    "9f54dc4a-260b-4842-87b5-e4bdfbfd7983"
                    "25aa9ad9-d4e8-4a38-bf19-2beb5ed575cd"
                }
                transform: mtx44 = {
                    -1, 0, 2.38418579e-07, 0
                    0, 1, 0, 0
                    -2.38418579e-07, 0, -1, 0
                    3099.65845, 62.3458862, 3186.61157, 1
                }
                name: string = "group1"
            }
            0xc3dc99ab = null
            0x130d7c32 = null
            0x8c58bdac = null
            0xcf01696f = null
            0x4dcdb947 = null
            0xde5c9458 = null
            0x34d96d05 = null
            0x6ecf9d87 = null
            0x349bea99 = null
            0xf6c3fa45 = null
            0xc4ce4f45 = null
            0xc5186fc3 = null
            0xc0536bdc = null
            0x8ee8c36a = null
            0xcd29364c = null
            0x1caf8acf = null
            0xda7daa53 = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Set5/Board_Harmony"
    }
    0xfa85a465 = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/Set5_Harmony"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.701960802, 0.784313738, 0.839215696, 1 }
                sunDirection: vec3 = { -0.282401145, 0.861317694, -0.422352254 }
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
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/Set5_Harmony_Navgrid.aimesh_ngrid"
            }
            MapBakeProperties {
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/Set5_Harmony/LightGrid.TFT_ArenaSkin_Set5.dat"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            0xd1dec2e5 = 0x1044fefe
            0x07150c0d = 0x3255ffa2
            0x1d17e30c = 0xdbc1b627
            0xe6c096cc = 0xd0d2ba77
            0x201d46b4 = 0xa19d69d1
            0xb6c688ca = 0xaf8ee171
            0x483a6667 = 0x9b7502fa
            0xb25857f0 = 0x26d93709
            0x27207d26 = 0x520a2eaf
            0x7e0646d4 = 0x1c50d8ad
        }
    }
    0x4112ec52 = MapPointLightType {
        lightColor: vec4 = { 0.866666675, 0.80392158, 0.443137258, 1 }
        specular: bool = false
    }
    0xbea7d96e = MapPointLightType {
        lightColor: vec4 = { 0.905882359, 0.90196079, 0.854901969, 1 }
        Impact: i32 = 1
    }
    0xe81e6598 = MapPointLightType {
        lightColor: vec4 = { 1, 0.58431375, 0, 1 }
        radius: f32 = 941
    }
    0x9e87f2f2 = MapPointLightType {
        lightColor: vec4 = { 1, 0, 0.0980392173, 1 }
        radius: f32 = 550
        specular: bool = false
    }
}
