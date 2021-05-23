#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Glaciers_Galaxies_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Glaciers_Galaxies_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Glaciers_Galaxies_A.TFT_ArenaSkin_Galaxy1.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Middle_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Middle_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_middle_A.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Floaty_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Floaty_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "Diffuse_Texture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Floaty_A.TFT_ArenaSkin_DarkStar.dds"
                addressW: u32 = 1
            }
        }
        paramValues: list[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Translate_Range"
                value: vec4 = { 0, 50, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bobbing_Rate"
                value: vec4 = { 0.300000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Secondary_Rotation_Rate"
                value: vec4 = { 0.138999999, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "RotationalAxis_Primary"
                value: vec4 = { 0.5, 0, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "RotationAngle_Primary"
                value: vec4 = { -0.0199999996, 0.0199999996, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "RotationAngle_Secondary"
                value: vec4 = { -0.0799999982, 0.0799999982, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "RotationalAxis_Secondary"
                value: vec4 = { 0.699999988, 1, -0.300000012, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Translate_Axis"
                value: vec4 = { 0, 1, 0, 0 }
            }
        }
        switches: list[embed] = {
            StaticMaterialSwitchDef {
                name: string = "USE_RANDOM_SECONDARY_MOTION"
            }
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = "Shaders/StaticMesh/ENV_FloatingObjects"
                    }
                }
            }
        }
        0xe251b20a: bool = false
    }
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Bench_Slab_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Bench_Slab_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Bench_Slab_A.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Flat_Top_C_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Flat_Top_C_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Flat_Top_C.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Blackhole_Rock_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Blackhole_Rock_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Blackhole_Rock_A.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Tall_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Darkstar/Materials/Default/Rock_Tall_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Darkstar/Textures/Rock_Tall_A.TFT_ArenaSkin_DarkStar.dds"
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
    "Maps/KitPieces/TFT/Galaxy/Materials/Default/Goldmine_Base_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Galaxy/Materials/Default/Goldmine_Base_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/Goldmine_Base_A.TFT_ArenaSkin_Galaxy1.dds"
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
    "Maps/KitPieces/TFT/Galaxy/Materials/Default/Board_CrashSite_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Galaxy/Materials/Default/Board_CrashSite_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Galaxy/Textures/Board_CrashSite_A.TFT_ArenaSkin_Galaxy1.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Metal_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Trim_Sheet_Metal_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Trim_Sheet_Metal_A.TFT_ArenaSkin_Galaxy2.dds"
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
    "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_Clean_A_MAT" = StaticMaterialDef {
        name: string = "Maps/KitPieces/TFT/Odyssey/Materials/Default/Jet_Clean_A_MAT"
        type: u32 = 0
        defaultTechnique: string = "normal"
        samplerValues: list[embed] = {
            StaticMaterialShaderSamplerDef {
                samplerName: string = "DiffuseTexture"
                textureName: string = "ASSETS/Maps/KitPieces/TFT/Odyssey/Textures/Jet_Clean_A.TFT_ArenaSkin_Odyssey.dds"
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
    "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Engine" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 1000
        particleName: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Engine"
        particlePath: string = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Engine"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_crashsite_jet_engine"
    }
    "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Alarm" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 1000
        particleName: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Alarm"
        particlePath: string = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Alarm"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_crashsite_jet_alarm"
    }
    "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Sparking" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 1000
        particleName: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Sparking"
        particlePath: string = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Sparking"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_crashsite_jet_sparking"
    }
    "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Skybox_CrashSite_A" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Base"
                importance: u8 = 2
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, -150, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_BackgroundClouds.TFT_ArenaSkin_DarkStar.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.97647059, 0.53725493, 0.874509811, 1 }
                }
                pass: i16 = -10
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 4
                isGroundLayer: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.349999994, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/Odyssey/Odyssey_Skybox_Stars01.dds"
                texDiv: vec2 = { 2, 2 }
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
                emitterName: string = "BlueClouds"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 150, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_MidgroundClouds.TFT_ArenaSkin_DarkStar.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.859998465, 0.300007641, 0.579995394 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.310002297, 0.680003047, 0.439993888 }
                }
                pass: i16 = -8
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -90, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.0799999982, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.270000011, 0.270000011, 0.270000011 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_BlueCloud.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.0199999996, 0 }
                }
                texDiv: vec2 = { 1, 2 }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.800000012, 2 }
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
                emitterName: string = "Pink01"
                disabled: bool = true
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 180, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_ForegroundClouds.TFT_Set3_Carousel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.859998465, 0.540001512, 1, 0.340001523 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.829999208, 0.889997721, 1 }
                }
                pass: i16 = -7
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 6, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { -0.100000001, 0 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 2 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud_Mask.dds"
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
                emitterName: string = "Pink02"
                disabled: bool = true
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 180, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_ForegroundClouds.TFT_Set3_Carousel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.200000003, 0.990005314, 1, 0.379995435 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.349996179, 0.910002291, 1, 0.420004576 }
                }
                pass: i16 = -6
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -10, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.200000003, 0.200000003, 0.200000003 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud.dds"
                textureMult: string = "ASSETS/Maps/Particles/TFT/DarkStar/Darkstar_Skybox_PinkCloud_Mask.dds"
                uvScaleMult: embed = ValueVector2 {
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
                emitterName: string = "Glow"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -6000, 0 }
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 150, -10 }
                    }
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1.29999995, 0, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Maps/Particles/TFT/DarkStar/TFT_Skybox_BackgroundClouds_B.TFT_Set3_Carousel.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.972549021, 0.972549021, 0.972549021, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.305882365, 0.31764707, 1 }
                }
                pass: i16 = -9
                miscRenderFlags: u8 = 4
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.170000002, 0.170000002, 0.170000002 }
                }
                texture: string = "ASSETS/Maps/Particles/TFT/DarkStar/DarkStar_Skybox_Clouds_Glow.dds"
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 2, 2 }
                }
                textureMult: string = "ASSETS/Maps/Particles/TFT/DarkStar/DarkStar_Skybox_BlueCloud_Mask.dds"
                scaleOverride: vec3 = { 17, 17, 17 }
            }
        }
        visibilityRadius: f32 = 12000
        particleName: string = "TFT_Skybox_CrashSite_A"
        particlePath: string = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Skybox_CrashSite_A"
        flags: u8 = 197
        hudAnchorPositionFromWorldProjection: bool = false
    }
    "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_RadioFutz" = VfxSystemDefinitionData {
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
        visibilityRadius: f32 = 1000
        particleName: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_RadioFutz"
        particlePath: string = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_RadioFutz"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_crashsite_radio_futz"
    }
    "Maps/Particles/TFT/Galaxy/Common/TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop" = VfxSystemDefinitionData {
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
        particleName: string = "TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop"
        particlePath: string = "Maps/Particles/TFT/Galaxy/Common/TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop"
        soundPersistentDefault: string = "Play_sfx_tft_env_galaxy_common_amb_loop"
    }
    "Maps/Particles/TFT/Shared/TFT_Wind" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 12
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
                            12
                        }
                    }
                }
                particleLinger: option[f32] = {
                    2
                }
                emitterName: string = "Wind"
                disabled: bool = true
                importance: u8 = 0
                shape: embed = VfxShape {
                    birthTranslation: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 1 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Env_MB_highWind_01.sco"
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
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 45, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 1, 3 }
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
                                    3
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 10, 1, 3 }
                        }
                    }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_highWind_01.SRE_Base.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.5
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
                            { 1, 1 }
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
                textureMult: string = "ASSETS/Particles/ChoDino_Dust.dds"
                birthUvScrollRateMult: embed = ValueVector2 {
                    constantValue: vec2 = { 0.400000006, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
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
                emitterName: string = "Wind1"
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
                        mSimpleMeshName: string = "ASSETS/Shared/Particles/Env_MB_bridgeWind_SE_02.SRE_Base.sco"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.611764729, 0.333333343, 1 }
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
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10.5, 4.5, 7.5 }
                }
                texture: string = "ASSETS/Shared/Particles/Env_MB_bridgeWind_SE_02.SRE_Base.dds"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.449999988, 0 }
                }
            }
        }
        visibilityRadius: f32 = 1500
        particleName: string = "TFT_Wind"
        particlePath: string = "Maps/Particles/TFT/Shared/TFT_Wind"
    }
    0x062cf158 = MapPointLightType {
        lightColor: vec4 = { 0.521568656, 0.450980395, 0.305882365, 1 }
        radius: f32 = 700
        Impact: i32 = 1
    }
    0x10e4d49d = MapPointLightType {
        lightColor: vec4 = { 0.0666666701, 0.282352954, 1, 1 }
        radius: f32 = 10000
    }
    0x4ddca076 = MapPointLightType {
        radius: f32 = 800
        Impact: i32 = 1
    }
    0x52248cce = MapPointLightType {
        lightColor: vec4 = { 0.690196097, 0.227450982, 0.772549033, 1 }
        radius: f32 = 963
        castStaticShadows: bool = false
    }
    0x7ca5e4f1 = MapPointLightType {
        lightColor: vec4 = { 0.105882354, 0.321568638, 0.713725507, 1 }
        radius: f32 = 1096
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0xae60cac5 = MapPointLightType {
        lightColor: vec4 = { 0.717647076, 0.211764708, 0.329411775, 1 }
        radius: f32 = 497
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    0xf232d9bd = MapPointLightType {
        lightColor: vec4 = { 0.749019623, 0.549019635, 0.443137258, 1 }
        radius: f32 = 941
        castStaticShadows: bool = false
        Impact: i32 = 1
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_CrashSite" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x230f76c9 = null
            0xc2883d97 = null
            0xa7782e5e = null
            0x696b2949 = null
            0x71bb40e9 = null
            0xc0a807f8 = null
            0xb4d8fce1 = null
            0xdb636f8c = null
            0xbe12b5c0 = null
            0x699d381c = null
            0x81800c07 = null
            0xe93e622f = null
            0x6e9b102a = null
            0xc7381247 = null
            0x05c14044 = null
            0x28b0e09e = null
            0x8eb233e1 = null
            0x1d669bba = null
            0x249af368 = null
            0x231252c6 = null
            0xa84b991f = null
            0xcf966981 = null
            0x880b009e = null
            0xbfcaffbd = null
            0xcd00a544 = null
            0xc603ee36 = null
            0x402ef86e = null
            0xf3d6a88b = null
            0xfcd52e23 = null
            0x8c3a34a7 = null
            0xe340c349 = null
            0xbdc026f1 = null
            0x7585ac88 = null
            0xfd8bb1ed = null
            0xd8597ad9 = null
            0x012abc46 = null
            0xe9c7571f = null
            0xc55fddac = null
            0x81141a89 = null
            0xbb25bb87 = null
            0xab083cb1 = null
            0x9b3a104b = null
            0x8ce1282a = null
            0xcc378a65 = null
            0x06fbf772 = null
            0xf2ce14d1 = null
            0x7eba57b9 = null
            0xd068048a = null
            0x7f3b1556 = null
            0xd014c231 = null
            0x2a85e648 = null
            0xbbcc2682 = null
            0x566bf092 = null
            0xc382436f = null
            0x960758d5 = null
            0xb04611c6 = null
            0x3c324535 = null
            0x9d517624 = MapGroup {
                members: list2[string] = {
                    "b09154bd-9858-441e-9dd6-a6c16938b58d"
                    "52a2df71-b46a-4c31-b98b-bbaf3f9c3060"
                }
                transform: mtx44 = {
                    0.321980417, 0, -0.946746349, 0
                    0, 1, 0, 0
                    0.946746349, 0, 0.321980417, 0
                    2691.39966, -96.5019226, 2694.24951, 1
                }
                name: string = "group2"
            }
            0x29756a34 = MapGroup {
                members: list2[string] = {
                    "021a87e0-675e-4f23-922d-b97c2247349f"
                }
                transform: mtx44 = {
                    0.883441567, 0, 0.468541414, 0
                    0, 1, 0, 0
                    -0.468541414, 0, 0.883441567, 0
                    3018.7854, -336.793213, 2764.20605, 1
                }
                name: string = "group3"
            }
            0x41d76ebe = null
            0x7b1263fb = null
            0x3cf2d8a2 = null
            0x270ed3f2 = null
            0x26fe0fed = null
            0xd4a6cfd0 = MapGroup {
                members: list2[string] = {
                    "3c23acd7-5130-4718-95a7-46b226959c7d"
                    "85c1e692-bffd-4793-a743-0875f54e9755"
                    "415d946f-7eff-471c-a203-05102e6fa61c"
                    "5b369070-ae43-4084-b75b-b27fc20a1b1a"
                    "2a84664a-f13c-4322-900d-25c03634f50a"
                }
                transform: mtx44 = {
                    0.54468751, 0.180444852, 1.10048509, 0
                    0.205838516, 1.18742681, -0.296580791, 0
                    -1.09601927, 0.31268084, 0.491207391, 0
                    3124.32959, -97.1662979, 2923.45093, 1
                }
                name: string = "group4"
            }
            0xab55b010 = null
            0xcd516da5 = null
            0xd912208f = null
            0x176da67d = null
            0x8eb9b05d = MapGroup {
                members: list2[string] = {
                    "52eab82f-9a3d-4b73-9798-fd19726f3c97"
                }
                transform: mtx44 = {
                    0.955328107, 0, 0.295547277, 0
                    0, 1, 0, 0
                    -0.295547277, 0, 0.955328107, 0
                    2654.55884, -24.8466644, 2364.62012, 1
                }
                name: string = "group6"
            }
            0xbbfb6b16 = null
            0x86acf049 = null
            0x73705834 = null
            0x1b0c92b4 = null
            0x1bebe5de = null
            0x74855342 = null
            0x105ec906 = null
            0xfce96f5c = null
            0x6ca9bb39 = null
            0x2e47a962 = null
            0x963522f2 = null
            0x1f1ab019 = null
            0x67daa41d = null
            0xa1c50e2a = null
            0xf513cda8 = null
            0x23bd6761 = null
            0x3899b2ed = null
            0x96c4b17c = null
            0x743413c1 = null
            0x63cedcd1 = null
            0x53eecf32 = null
            0xd221f06b = null
            0x4a575b6d = null
            0x43f058a6 = null
            0x4e50b7e8 = null
            0xafce4019 = null
            0x804c3df6 = null
            0x05a3000e = null
            0xe3f22859 = null
            0x7630e502 = null
            0xc4ed6dd3 = null
            0x0315afbb = null
            0x4f61bd80 = null
            0x94eb79ff = null
            0xcaa07a5f = null
            0x2c98cc45 = null
            0xa1923f5f = null
            0x62fa0a5c = MapGroup {
                members: list2[string] = {
                    "7b7207a7-2db3-4fd2-81b7-af7b11bbbe1b"
                }
                transform: mtx44 = {
                    -0.972255707, 0, 0.233920604, 0
                    0, 1, 0, 0
                    -0.233920604, 0, -0.972255707, 0
                    1420.3446, -51.4022865, 2802.73901, 1
                }
                name: string = "group7"
            }
            0xfedd1e9c = null
            0xccce231b = null
            0xa21d2ddf = null
            0x4f5e4d3e = null
            0x544363ef = null
            0xff0e8ffa = null
            0xd0e5b659 = null
            0xac14d302 = null
            0x1eecc059 = null
            0x049f72c6 = null
            0x325ab660 = null
            0x58b90ce7 = null
            0xc2a45041 = null
            0xf16f19ad = null
            0xea427ab9 = null
            0x8961c151 = null
            0xfd4e4e46 = null
            0x80d68bad = null
            0x95fce23f = null
            0xa00974a2 = null
            0x9e4c5c92 = null
            0x4461221c = null
            0xe50c0990 = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_CrashSite"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Shared" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x2ff7cdaf = null
            0x280cca76 = null
            0x8428f883 = null
            0xe30670d4 = null
            0x2b87a377 = null
            0xbb931b41 = null
            0x4cbd628a = null
            0x42024cef = null
            0x53ed22c7 = null
            0x094349ef = null
            0xb1d8cef4 = null
            0xf4b61a8f = null
            0xab595e64 = null
            0x05717daa = null
            0x329adcec = null
            0x79acf00c = null
            0xf043b4b5 = null
            0xd6d5733c = null
            0xa8d44455 = null
            0x019b834d = null
            0x1d77da53 = null
            0xb7e917a0 = null
            0x9297418f = null
            0x3b47d4bd = null
            0x17bc3116 = null
            0xee65b0c2 = null
            0x35a36457 = null
            0xeff8da4b = null
            0x7a3df143 = null
            0x5d77c8c4 = null
            0x1a238f12 = null
            0xfe47d27d = null
            0x56565a88 = null
            0x5ca62bc1 = null
            0xc1006eb1 = null
            0x9bd2715d = null
            0x30c93fa1 = null
            0x7d0e7eab = null
            0x3cd8e0f7 = null
            0x42e3d592 = null
            0xbb52d822 = null
            0x3467a2ff = null
            0xb4c99a87 = null
            0x20ca2a2c = null
            0x5b9cd197 = null
            0x434c84c3 = null
            0x52bbeec2 = null
            0x41c52df6 = null
            0x7399c8da = null
            0xefebf928 = null
            0x7551669f = null
            0x6158c9cf = null
            0x2a7774db = null
            0xa4682294 = null
            0x35e6a257 = MapGroup {
                members: list2[string] = {
                    "c451d051-0d2c-4840-91db-65cfd0df1ec1"
                    "26320d51-b0c6-4d9e-adcd-c3d70889d47d"
                }
                name: string = "group15"
            }
            0x44ff912f = null
            0x3e7970d3 = null
            0x25191500 = null
            0xd4fe640a = MapGroup {
                members: list2[string] = {
                    "73947327-75ac-4800-a52d-47e55caf6a79"
                    "9b30e97a-0edf-4cc1-8a73-3cf21c10dd03"
                    "8baed65f-fb57-4b67-ac97-06a00c57a686"
                    "ce2b35da-f683-4a24-8e5c-c34d4dcb6230"
                }
                name: string = "group19"
            }
            0x5ceac25e = null
            0xca57d935 = null
            0xd675623d = null
            0x7472518f = null
            0xc09e1860 = null
            0x3b78fc17 = null
            0x55126cee = null
            0xbbbf5dc0 = null
            0x757650c5 = null
            0xbf1f198e = null
            0xfaef2fbb = null
            0xe855532b = null
            0x920c4873 = null
            0xfcceb49c = null
            0xd7472490 = null
            0x38c82321 = null
            0x59e7c7ef = null
            0xa632e126 = null
            0x4a3bc502 = null
            0xebb4e9b7 = null
            0x649d4d0c = null
            0xba60e39c = null
            0xa8f7297b = null
            0xb9c1383c = null
            0x8f60e8ce = null
            0xbb0e8c04 = null
            0x50442457 = null
            0x537b4715 = null
            0x59c7108b = null
            0x60bc0146 = null
            0xe525996b = null
            0x13d941ee = null
            0x453319f6 = null
            0x6c4a33d5 = null
            0x302c2c48 = null
            0x142d9399 = null
            0x67613649 = null
            0x29d03e8c = null
            0x11763954 = null
            0xe6806b2a = null
            0x4eec50de = null
            0xec7ee90d = null
            0x245334ad = null
            0x5d148095 = null
            0xb8b46272 = null
            0xb19fcaf8 = null
            0xebe9512f = null
            0x953ab1a9 = null
            0xc71b37f3 = null
            0x1d409379 = MapGroup {
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 0.948094666, 0
                    2995.67822, -339.70752, 2667.89282, 1
                }
                name: string = "group1"
            }
            0x9093d129 = null
            0x45fb23c1 = null
            0xe873784e = null
            0x91603791 = null
            0x3fdf3804 = null
            0xb3299236 = null
            0x235b2294 = null
            0xcc475dcc = null
            0x53aae39c = null
            0xe4b79064 = null
            0xe89a5db0 = null
            0x235bf9ba = null
            0xc7537449 = null
            0xd248423b = null
            0x7353ff5b = null
            0x118a5998 = null
            0x6ef00b3d = null
            0x4fda4f08 = null
            0x2a763665 = null
            0x43bd56ab = null
            0x92469741 = null
            0xc4925fe5 = null
            0x12302de6 = null
            0x3b720783 = null
            0xd8d13bb3 = MapGroup {
                members: list2[string] = {
                    "23ab19f5-6c49-46c8-83c5-474913178f5c"
                    "eb1f8eed-3f53-4fd7-81f1-a30cddf7626f"
                    "a35e5b65-ce0e-459d-a63e-dab864818dcb"
                    "e10cb0a9-4f41-4577-96f1-28d6648e42f2"
                    "7443d31c-69a4-40eb-b899-cfe065714df9"
                    "5e1ba055-eb3d-4a37-b29c-13cceff43f26"
                    "36ba2e5f-890e-4fb2-95ce-12883f3b0275"
                    "64944ff3-77cf-43a0-a53b-433d306ce246"
                    "e000be44-9aa7-4e63-a027-9fdcfece4a64"
                    "a5c3ec42-64cf-458b-a973-d692cb93f30c"
                }
                transform: mtx44 = {
                    -3.57627869e-07, 0, 1, 0
                    0, 1, 0, 0
                    -1, 0, -3.57627869e-07, 0
                    1699.83521, -118.505661, 409.408142, 1
                }
                name: string = "group5"
            }
            0xa6f078fa = null
            0xadd350c9 = null
            0x56b79bfe = null
            0xbc4d3603 = null
            0x9c6278b9 = null
            0xcf2d26a9 = null
            0x1c3b32ad = null
            0x4594fd09 = null
            0xbd178575 = null
            0x70bd1a2e = null
            0xd17f1116 = null
            0x7ca7fe0f = null
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Shared"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_CrashSite" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xb7ce048b = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.841669142
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2198.21289, -322.215271, 674.152649, 1
                }
                name: string = "Freljord_FG_Torch1"
            }
            0xd4d9273a = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.841669142
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1956.45264, -416.294373, 3624.71655, 1
                }
                name: string = "Freljord_FG_Torch3"
            }
            0x49a55217 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.644464135
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3810.53467, -391.470093, 2606.39697, 1
                }
                name: string = "Freljord_FG_Torch4"
            }
            0xc5b41e5c = MapPointLight {
                type: link = 0x4ddca076
                radiusScale: f32 = 0.999999881
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2506.0957, 804.190735, 115.258636, 1
                }
                name: string = "Light_Point_Center_DragonCloud15"
            }
            0x1afee984 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.735546291
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2936.1665, -395.772461, 439.205261, 1
                }
                name: string = "Freljord_FG_Torch5"
            }
            0x46b9a2bf = MapPointLight {
                type: link = 0x062cf158
                radiusScale: f32 = 0.891021967
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1140.05054, 358.194794, 1433.90369, 1
                }
                name: string = "Light_Yellow_01_2"
            }
            0xffe17815 = MapPointLight {
                type: link = 0x062cf158
                radiusScale: f32 = 0.891021729
                intensityScale: f32 = 1.75
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2865.42993, 344.704224, 2652.13599, 1
                }
                name: string = "Light_Yellow_01_3"
            }
            0xc4d3ca8c = MapPointLight {
                type: link = 0x062cf158
                radiusScale: f32 = 1.44341075
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1906.13977, 351.985992, 1081.46448, 1
                }
                name: string = "Light_Yellow_01_4"
            }
            0x6d9eb26f = MapPointLight {
                type: link = 0x062cf158
                radiusScale: f32 = 1.44341075
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1995.22986, 351.985992, 3014.03101, 1
                }
                name: string = "Light_Yellow_01_5"
            }
            0x080fb9e6 = MapPointLight {
                type: link = 0xf232d9bd
                radiusScale: f32 = 1.26256442
                intensityScale: f32 = 1.5
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2000.11597, 437.052002, 2033.03796, 1
                }
                name: string = "Freljord_AV_Center1"
            }
            0xbc635310 = MapPointLight {
                type: link = 0x10e4d49d
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1879.6344, 5000, 1708.02978, 1
                }
                name: string = "Light_Point_AmbientDeepOcean_DragonOcean1"
            }
            0x7020ef8d = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.764788151
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3951.25635, -186.254105, 1455.34644, 1
                }
                name: string = "Freljord_WC_Blue_Fill1"
            }
            0xbc0b53c6 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.764787912
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2258.81494, -186.254105, 656.771484, 1
                }
                name: string = "Freljord_WC_Blue_Fill2"
            }
            0xfb1c9496 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.750159621
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1875.78345, -174.925659, 3639.51782, 1
                }
                name: string = "Freljord_WC_Blue_Fill4"
            }
            0xe2cd6db1 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 0.764787912
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3944.10767, -186.254105, 2571.77759, 1
                }
                name: string = "Freljord_WC_Blue_Fill5"
            }
            0x015b3389 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 1.6396029
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    982.884888, 267.677185, 3573.90698, 1
                }
                name: string = "Freljord_FG_Fill1"
            }
            0xcf381eea = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 1.89963698
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2670.98144, 289.476013, 3688.99634, 1
                }
                name: string = "Freljord_FG_Fill2"
            }
            0xe2a41f4c = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 1.70631826
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2956.29688, 583.493042, 1413.16748, 1
                }
                name: string = "Freljord_FG_Fill3"
            }
            0x0d5b8f90 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 1.6396029
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1299.99634, 192.908081, 638.927307, 1
                }
                name: string = "Freljord_FG_Fill4"
            }
            0x9dc387ff = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 1.18850601
                intensityScale: f32 = 1.25
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    554.995361, 362.144775, 654.155701, 1
                }
                name: string = "Freljord_WC_Blue_Fill6"
            }
            0xd0969ff0 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.841669142
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    105.50354, -322.215271, 1177.60095, 1
                }
                name: string = "Freljord_FG_Torch6"
            }
            0xf00f49bb = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 1.08588922
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3789.91772, 257.138855, 3349.78467, 1
                }
                name: string = "Freljord_WC_Blue_Fill7"
            }
            0x48239047 = MapPointLight {
                type: link = 0x52248cce
                radiusScale: f32 = 0.644464135
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3591.05078, -213.755356, 2916.97339, 1
                }
                name: string = "Freljord_FG_Torch7"
            }
            0xe863d6c8 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 1.36984897
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    3771.3833, 761.031006, 1888.60644, 1
                }
                name: string = "Freljord_WC_Blue_Fill8"
            }
            0x34533306 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 1.46964693
                intensityScale: f32 = 1.29999995
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -384.594971, 282.4776, 1391.97278, 1
                }
                name: string = "Freljord_WC_Blue_Fill9"
            }
            0xb9e66ab5 = MapPointLight {
                type: link = 0xae60cac5
                radiusScale: f32 = 3.27487636
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    -215.669373, 1323.02905, 2391.27197, 1
                }
                name: string = "Freljord_FG_Fill5"
            }
            0x05e69834 = MapPointLight {
                type: link = 0x7ca5e4f1
                radiusScale: f32 = 1.36984897
                intensityScale: f32 = 1.10000002
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    394.627502, 416.356384, 3222.93726, 1
                }
                name: string = "Freljord_WC_Blue_Fill3"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_CrashSite"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_CrashSite" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x64eb94c9 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/Common/TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1868.32385, 151.125488, 2276.11743, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_Outdoor_Amb_Loop1"
            }
            0x75b783cb = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_RadioFutz"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1240.54639, -6.10351562e-05, 1689.77808, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_RadioFutz1"
            }
            0x2ffc388e = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Sparking"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1134.70581, 130.737122, 1834.13306, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Sparking1"
            }
            0x0e38859e = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Alarm"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1150.68738, 80.9458008, 1486.78577, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Alarm1"
            }
            0x5470e172 = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Engine"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    995.01355, 4.29052734, 1646.20325, 1
                }
                name: string = "TFT_Audio-Emitter_Galaxy_CrashSite_Jet_Engine1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_CrashSite"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy/Art_CrashSite_Skybox" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0x36ee18be = MapParticle {
                system: link = "Maps/Particles/TFT/Galaxy/CrashSite/TFT_Skybox_CrashSite_A"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1987.25806, 0.0009765625, 2051.75488, 1
                }
                name: string = "TFT_Skybox_CrashSite_A1"
                0xccf79327: u8 = 126
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy/Art_CrashSite_Skybox"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy_Design_Base" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xf7e857de = MapLocator {
                0xad304db5: string = "EditorData/Maps/Locators/Locator_Spawn_Green"
                sceneLayer: string = "Locators"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    2942.92432, 11.2485962, 2437.69849, 1
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
                    1067.23218, 11.2485962, 1695.15454, 1
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
                    2995.97485, 0, 2859.89062, 1
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
                    943.477173, 0, 1180.83337, 1
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
                    1102.27698, 0, 1388.43628, 1
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
                    2857.91894, 0, 2664.4563, 1
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
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy_Design_Base"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_CrashSite" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xfda23b15 = MapParticle {
                system: link = "Maps/Particles/TFT/Shared/TFT_Wind"
                transform: mtx44 = {
                    1, 0, 0, 0
                    0, 1, 0, 0
                    0, 0, 1, 0
                    1919.56641, 0.000244140625, 1987.96899, 1
                }
                name: string = "TFT_Wind1"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_CrashSite"
    }
    "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_CrashSite" = MapPlaceableContainer {
        items: map[hash,pointer] = {
            0xda436347 = MapLightingVolume {
                sunColor: vec4 = { 0.721568644, 0.53725493, 0.309803933, 0.972549021 }
                sunDirection: vec3 = { 0.150000006, 0.827000022, 0.150000006 }
                0xd8851203: f32 = 15
                0xba02f116: f32 = 0.100000001
                skyLightColor: vec4 = { 0.784313738, 0.592156887, 0.525490224, 1 }
                horizonColor: vec4 = { 0.623529434, 0.56078434, 0.819607854, 1 }
                groundColor: vec4 = { 0.737254918, 0.572549045, 0.615686297, 1 }
                skyLightScale: f32 = 0.800000012
                lightMapColorScale: f32 = 2
                fogColor: vec4 = { 0.13333334, 0.101960786, 0.149019614, 1 }
                fogAlternateColor: vec4 = { 0.262745112, 0.117647059, 0.156862751, 1 }
                fogStartAndEnd: vec2 = { 250, -600 }
                transform: mtx44 = {
                    2835.39404, 0, 0, 0
                    0, 4314.72998, 0, 0
                    0, 0, 3081.94995, 0
                    2186.59424, -927.355957, 2144.35596, 1
                }
                name: string = "LightingVolume2"
            }
        }
        path: string = "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_CrashSite"
    }
    "Maps/MapGeometry/Map22/Galaxy_CrashSite" = mapContainer {
        mapPath: string = "Maps/MapGeometry/Map22/Galaxy_CrashSite"
        components: list[pointer] = {
            MapSunProperties {
                sunColor: vec4 = { 0.34117648, 0.266666681, 0.529411793, 1 }
                sunDirection: vec3 = { -0.385433108, 0.828491211, -0.406255662 }
                0xd8851203: f32 = 75
                skyLightColor: vec4 = { 0.482352942, 0.521568656, 0.741176486, 1 }
                horizonColor: vec4 = { 0.321568638, 0.286274523, 0.509803951, 1 }
                groundColor: vec4 = { 0.368627459, 0.219607845, 0.392156869, 1 }
                skyLightScale: f32 = 1
                fogEnabled: bool = false
                fogColor: vec4 = { 0.100007631, 0.059998475, 0.110002287, 1 }
                fogAlternateColor: vec4 = { 0.420004576, 0.379995435, 0.420004576, 1 }
                fogStartAndEnd: vec2 = { -1000, -20000 }
                fogEmissiveRemap: f32 = 1
                useBloom: bool = true
            }
            MapBakeProperties {
                0x22d24a9a: f32 = 0.850000024
                lightGridCharacterFullBrightIntensity: f32 = 0.5
                0x2f3b5471: f32 = 2
                lightGridFileName: string = "ASSETS/Maps/Lightmaps/Maps/MapGeometry/Map22/Galaxy_CrashSite/LightGrid.TFT_1023_LightingUpdate.dat"
            }
            MapLightingV2 {
                0xee91017d: f32 = 0.899999976
            }
            MapNavGrid {
                0xf7197db9: string = "ASSETS/Maps/NavGrid/Map22/Galaxy_CrashSite_Navgrid.aimesh_ngrid"
            }
        }
        boundsMax: vec2 = { 4000, 4000 }
        0xf010defb: f32 = 5000
        chunks: map[hash,link] = {
            "Galaxy_Design_Base" = "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy_Design_Base"
            0x32425435 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_Shared"
            0x053f9f57 = "Maps/MapGeometry/Map22/Chunks/Galaxy/LightingVolume_CrashSite"
            0x81567299 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Lighting_CrashSite"
            0x4c8d7677 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Audio_CrashSite"
            0x03ea6631 = "Maps/MapGeometry/Map22/Chunks/Galaxy/VFX_CrashSite"
            0xd1db3240 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Art_CrashSite"
            0x0ce3da92 = "Maps/MapGeometry/Map22/Chunks/Galaxy/Galaxy/Art_CrashSite_Skybox"
        }
    }
}
