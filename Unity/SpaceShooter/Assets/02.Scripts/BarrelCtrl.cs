using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BarrelCtrl : MonoBehaviour
{
    // 폭발 효과 파티클을 연결할 변수
    public GameObject expEffect;

    public Texture[] textures;

    private new MeshRenderer renderer;

    //폭발 반경
    public float radius = 10.0f;

    // 컴포넌트를 저장할 변수
    private Transform tr;
    private Rigidbody rb;

    //총알 맞은 횟수를 누적시킬 변수
    private int hitCount = 0;

    Collider[] colls = new Collider[10];

    // Start is called before the first frame update
    void Start()
    {
        tr = GetComponent<Transform>();
        rb = GetComponent<Rigidbody>();

        renderer = GetComponentInChildren<MeshRenderer>();

        int idx = Random.Range(0, textures.Length);

        renderer.material.mainTexture = textures[idx];
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.collider.CompareTag("BULLET"))
        {
            //총알 맞은 횟수를 증가시키고 3회 이상이면 폭발 처리
            if(++hitCount == 3)
            {
                ExpBarrel();
            }
        }
    }

    void ExpBarrel()
    {
        //폭발 효과 파티클 생성
        GameObject exp = Instantiate(expEffect, tr.position, Quaternion.identity);

        Destroy(exp, 5.0f);

        //rb.mass = 1.0f;
        //rb.AddForce(Vector3.up * 1500.0f);


        //간접 폭발력 전달
        IndirectDamage(tr.position);


        Destroy(gameObject, 3.0f);
    }

    void IndirectDamage(Vector3 pos)
    {
        //Collider[] colls = Physics.OverlapSphere(pos, radius, 1 << 3);
        Physics.OverlapSphereNonAlloc(pos,
                                      radius,
                                      colls,
                                      1 << 3);

        foreach(var coll in colls)
        {
            rb = coll.GetComponent<Rigidbody>();
            rb.mass = 1.0f;

            rb.constraints = RigidbodyConstraints.None;

            rb.AddExplosionForce(1500.0f, pos, radius, 1200.0f);
        }
    }
}
