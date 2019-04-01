$(function () {

    var signup = '';
    var fields = ['email'];
    var public_key_field_name = 'username';
    if (tp.isConnected()) {
        if (window.is_login) return true;
        var account;
        tp.getCurrentWallet().then(function (result) {
            account = result['data']['name'];
            const sign_param = {
                from: account,
                publicKey: result['data']['address'],
                signdata: '172.16.16.24'
            };
            const public_key = result['data']['address'];
            tp.eosAuthSign(sign_param).then(function (result) {
                const sign_data = result['data']['timestamp'] + result['data']['wallet']
                    + result['data']['signdata'] + result['data']['ref'];

                $("#d1").append(sign_data);
                $.post('/api/v1/sign_up', {
                    'sign': result['data']['signature'],
                    'public_key': public_key,
                    'sign_data': sign_data,
                    'name': account,
                    'source': 2
                }, function (data) {
                    if (data['succ']) window.location.reload();
                })
            });
        });
    } else {
        const main_network = {
            blockchain: 'eos',
            protocol: 'http',
            host: 'et.steamao.com',
            port: 11223,
            chainId: 'cf057bbfb72640471fd910bcb67639c22df9f92470936cddc1ade0e2f2e7dc4f'
        };
        ScatterJS.scatter.connect("farm").then(connected => {
            if (!connected) return false;
            window.scatter_core = ScatterJS.scatter;
            window.ScatterJS = null;
            window.scatter = null;
            // scatter_core.getVersion().then(x => console.log(x));
        });

        $("#login").on('click', function () {
            if (scatter_core.identity) {
                web_login();
            } else {
                requestIdentity(fields, public_key_field_name, signup, main_network, console.log);
            }
        });

        async function requestIdentity(requiredFields, pubkeyFieldName, signup_url, network, onIdentityReject) {
            let identitySettings = {
                personal: ['firstname'],
            };
            if (network) {
                await scatter_core.suggestNetwork(network);
                identitySettings['accounts'] = [network];
            }

            scatter_core.getIdentity(identitySettings).then((identity) => {
                console.log(identity);
                web_login();
            }).catch(error => {
                console.log("Identity or Network was rejected");
                if (typeof onIdentityReject === 'function') {
                    onIdentityReject(error);
                }
            })
        }

        function random12() {

            var arr = [];//容器
            for(var i =0; i<12;i++){//循环六次
                var num = Math.random()*9;
                num = parseInt(num, 10);
                arr.push(num);
            }
            return arr.join('');
        }

        function web_login() {
            // if (window.is_login) return true;
            var sign_data = random12();
            console.log(sign_data);
            scatter_core.authenticate(sign_data).then(signature => {
                console.log(signature);
                $.post('/api/v1/sign_up', {
                    'sign': signature,
                    'public_key': scatter_core.identity.publicKey,
                    'name': scatter_core.identity.accounts[0].name,
                    'sign_data': sign_data,
                    'source': 1,
                }, function (data) {
                    if (data['succ']) window.location.reload();
                })
            }).catch(signatureError => {
                console.log(signatureError);
            });
        }
    }
    console.log(location.hostname);

    $("#logout").on('click', function () {
        $.getJSON('/api/v1/logout', null, function (data) {
        });
        scatter_core.forgetIdentity();
    });

    $("#more").on('click', function () {
        scatter_core.authenticate().then(signature => {
            console.log(2, signature);
        }).catch(signatureError => {
            console.log(signatureError);
        });
    });

    $("#sign").on('click', function () {
        const publicKey = scatter_core.identity.publicKey;
        const data = random12();

        console.log(data, publicKey);

        scatter_core.getArbitrarySignature(publicKey, data).then(signature => {
            console.log(signature);
            $.post('/api/v1/sign_up', {
                    'sign': signature,
                    'public_key': publicKey,
                    'sign_data': data,
                    'name': scatter_core.identity.accounts[0].name,
                    'source': 2
                }, function (data) {
                    if (data['succ']) window.location.reload();
                })
        }).catch(error => {
            console.log(error);
        });
    });

});