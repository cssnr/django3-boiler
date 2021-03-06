#!/usr/bin/env groovy

@Library('jenkins-libraries')_

pipeline {
    agent {
        label 'jenkins-slave-docker'
    }
    options {
        buildDiscarder(logRotator(numToKeepStr:'5'))
        timeout(time: 1, unit: 'HOURS')
    }
    environment {
        DISCORD_ID = "discord-hook-smashed"
        COMPOSE_FILE = "docker-compose-swarm.yml"

        BUILD_CAUSE = getBuildCause()
        VERSION = getVersion("${GIT_BRANCH}")
        GIT_ORG = getGitGroup("${GIT_URL}")
        GIT_REPO = getGitRepo("${GIT_URL}")
        SERVICE_NAME = "${GIT_ORG}-${GIT_REPO}"
        NFS_HOST = "nfs01.cssnr.com"
        NFS_BASE = "/data/docker"
    }
    stages {
        stage('Init') {
            steps {
                echo "\n--- Build Details ---\n" +
                        "BUILD_CAUSE:   ${BUILD_CAUSE}\n" +
                        "GIT_BRANCH:    ${GIT_BRANCH}\n" +
                        "GIT_URL:       ${GIT_URL}\n" +
                        "JOB_NAME:      ${JOB_NAME}\n" +
                        "SERVICE_NAME:  ${SERVICE_NAME}\n" +
                        "COMPOSE_FILE:  ${COMPOSE_FILE}\n" +
                        "NFS_HOST:      ${NFS_HOST}\n" +
                        "VERSION:       ${VERSION}\n"
                verifyBuild()
                sendDiscord("${DISCORD_ID}", "Pipeline Started by: ${BUILD_CAUSE}")
                getConfigs("${SERVICE_NAME}")   // use this to get service configs from deploy-configs
            }
        }
        stage('Dev Deploy') {
            when {
                allOf {
                    not { branch 'master' }
                }
            }
            environment {
                ENV = "dev"
                ENV_FILE = "service-configs/services/${SERVICE_NAME}/${ENV}.env"
                STACK_NAME = "${ENV}_${SERVICE_NAME}"
                NFS_DIRECTORY = "${NFS_BASE}/${STACK_NAME}"
                TRAEFIK_HOST = "django3-boiler-dev.sapps.me"
            }
            steps {
                echo "\n--- Starting ${ENV} Deploy ---\n" +
                        "STACK_NAME:        ${STACK_NAME}\n" +
                        "NFS_DIRECTORY:     ${NFS_DIRECTORY}\n" +
                        "TRAEFIK_HOST:      ${TRAEFIK_HOST}\n" +
                        "ENV_FILE:          ${ENV_FILE}\n"
                sendDiscord("${DISCORD_ID}", "${ENV} Deploy Started")
                setupNfs("${STACK_NAME}")
                updateCompose("${COMPOSE_FILE}", "STACK_NAME", "${STACK_NAME}")
                stackPush("${COMPOSE_FILE}")
                stackDeploy("${COMPOSE_FILE}", "${STACK_NAME}")
                sendDiscord("${DISCORD_ID}", "${ENV} Deploy Finished")
            }
        }
        stage('Prod Deploy') {
            when {
                allOf {
                    branch 'master'
                    triggeredBy 'UserIdCause'
                }
            }
            environment {
                ENV = "prod"
                ENV_FILE = "service-configs/services/${SERVICE_NAME}/${ENV}.env"
                STACK_NAME = "${ENV}_${SERVICE_NAME}"
                NFS_DIRECTORY = "${NFS_BASE}/${STACK_NAME}"
                TRAEFIK_HOST = "django3-boiler.sapps.me"
            }
            steps {
                echo "\n--- Starting ${ENV} Deploy ---\n" +
                        "STACK_NAME:        ${STACK_NAME}\n" +
                        "NFS_DIRECTORY:     ${NFS_DIRECTORY}\n" +
                        "TRAEFIK_HOST:      ${TRAEFIK_HOST}\n" +
                        "ENV_FILE:          ${ENV_FILE}\n"
                sendDiscord("${DISCORD_ID}", "${ENV} Deploy Started")
                setupNfs("${STACK_NAME}")
                updateCompose("${COMPOSE_FILE}", "STACK_NAME", "${STACK_NAME}")
                stackPush("${COMPOSE_FILE}")
                stackDeploy("${COMPOSE_FILE}", "${STACK_NAME}")
                sendDiscord("${DISCORD_ID}", "${ENV} Deploy Finished")
            }
        }
    }
    post {
        always {
            cleanWs()
            script { if (!env.INVALID_BUILD) {
                sendDiscord("${DISCORD_ID}", "Pipeline Complete: ${currentBuild.currentResult}")
            } }
        }
    }
}
